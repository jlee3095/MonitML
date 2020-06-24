# MonitML

This repository contains the required files and write-up for Jason Lee's 2020 Insight DevOps project.

## Table of Contents
  - [1.0 Introduction](README.md#introduction)
  - [2.0 Tech stack](README.md#tech-stack)
  - [3.0 Demo](README.md#demo)
  - [4.0 Build Instructions](README.md#build-instructions)
  - [5.0 Conclusions](README.md#conclusions)

## Introduction
Machine Learning models can often have poor performance in production. Possible reasons of poor performing models in production may be attributed to differences between the data(features) used to train the models in development and the data(features) used to serve predictions in production. Furthermore, the model may have been trained on a data set that is completely different to what is found in production, reducing the predictive performance of the model. One other scenario that is possible is that the deployed model worked well in the past but has degraded over time due to changes in the environment. The world is not a static environment and for some use cases, ML models may need to be continuously retrained on newer data to have good predictive performance. In addition operational errors in production may occur due to "buggy" models or something as simple as accidently deploying the wrong model version. All of the described operational and predictive performance faults can decrease the business value of a ML service. 

To help reduce the time of finding errors in ML models in production as described above, I have created a tech stack in which the operational and predictive performance of machine learning models can be monitored in real-time. In addition, if bad performance is detected, an alert can also be triggered through Slack.

### Metrics to monitor
Both model and operational metrics should be monitored. Operational metrics could include operational success, latencies, traffic, and CPU/Memory/Disk usage. There are numerous model metrics that can be monitored and the decision of which model metrics will vary on the use case. Regardless of metrics used, the ultimate goal is to ensure that the predictions are correct. In some cases it is unfeasible to monitor predicition "correctness" due to the long time lag of finding out if the prediction matches reality. For example, a firm has created a model that can predicts if an individual has cancer. Finding out if the model predicted the right result may take considerable time and resources. Prediction range/average/distribution and input(feature) distribution may be good secondary metrics to monitor in the absence of measuring prediction "correctness".     


## Tech Stack
### Overview
The tech stack is built on top of Kubernetes (Amazon EKS). The infrastructure is built using Terraform and is properly configured using Helm. Machine Learning pipelines for training models can be built using KubeFlow and the models are served on Seldon Core. Seldon Core can expose metrics such as prediction range/average for Prometheus to detect in real-time and Grafana is used to visualize the metrics. Prometheus can also be configured to send alerts through AlertManager.       

![Fig 1: ML monitoring tech stack](/Images/techstack.PNG)


## Demo
For this demo, two different models that predict housing prices are deployed via canary method(75/25) using Seldon Core. One of the models has purposefully bad performance as the model it outputs a prediction of $100, regardless of the input. Since a housing price of $100 dollars is infeasible, a Slack notification is sent through Prometheus AlertManager. AlertManager is triggered to send an alert if the average housing price is less than $100,000.

The metrics can be visualized using Grafana. Metrics that are monitored for this demo include min/max/average prediction, operations per second for each model, and latencies for each model.

![Fig 2: Dashboard](/Images/dashboard.PNG)

![Fig 3: Alerting](/Images/alert.PNG)

## Build Instructions
### Prerequisites
The following software must be installed into your local environment:
* Terraform
* Helm
* AWS CLI
* Kfctl
* Kubectl

### Clone the repository:
`git clone https://github.com/jlee3095/MonitML.git`

### Build Infrastructure using Terraform: 
```sh
aws configure #ADD access key, secret access key, region(eg. us-east-2), and output formt (eg. json) when prompted
cd ./MonitML/terraform
terraform init
terraform apply #Type in "yes" when asked 
aws eks --region us-east-2 update-kubeconfig --name training-eks #Default name is training-eks and region is us-east-2. These can be changed in terraform files.
```
### Configure KubeFlow:
 ```sh
cd ~/MonitML
kfctl apply -V -f [INSERT PATH]/MonitML/kubeflow/kfctl_aws.v1.0.2_terraform.yaml
```
### Configure Seldon Core, Prometheus, and Grafana:
Install Seldon Core Operator
```sh
helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --set istio.enabled=true \
    --set istio.gateway=kubeflow-gateway \
    --namespace kubeflow
```
Install Seldon Core Grafana/Prometheus
```sh
helm install seldon-core-analytics [INSERT PATH]/MonitML/seldon-core-analytics-orig \
   --repo https://storage.googleapis.com/seldon-charts \
   --set alertmanager.config.enabled=true \
   --namespace kubeflow
```
Create a Canary Deployment that can be accessed by istio ingressgateway
```sh
kubectl create namespace seldon

cat <<EOF | kubectl create -n seldon -f - 
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: kubeflow-gateway
  namespace: seldon
spec:
  selector:
    istio: ingressgateway
  servers:
  - hosts:
    - '*'
    port:
      name: http
      number: 80
      protocol: HTTP
EOF

kubectl apply -f [INSERTPATH]/canary.json -n seldon
```

### Accessing Prometheus/Grafana/AlertManager: 
Access by going to localhost:300X where X is 0,1,5 depending on what service you would like to access
grafana login username:admin password:password
```sh
kubectl port-forward svc/seldon-core-analytics-prometheus-seldon 3001:80 -n kubeflow &
kubectl port-forward svc/seldon-core-analytics-grafana 3000:80 -n kubeflow &
kubectl port-forward svc/seldon-core-analytics-prometheus-alertmanager 3005:80 -n kubeflow &
```

### Sending Requests to Inference Server:
The bash script sends 60 requests to inference server
```sh
kubectl port-forward $(kubectl get pods -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}') -n istio-system 8004:80
PATH/MonitML/script
```
### In regards to creating custom metrics:
Custom metrics can be configured in python before wrapping with s2i. For examples see the model folder. In order to create a proper file you will need:
* Download s2i
* pip install seldon-core
* Download Docker
* Modelfile.py
* environment file
* requirements.txt file
* You must use s2i/seldonio/python3:1.1+ to be able to have a endpoint with custom metrics that can be exposed to prometheus 
```sh
# The python, env, requirments files must be in the same folder, cd to that folder
s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:1.1.0 [MODELNAME]:[TAG]

# To test model use contract.json
docker run -d --rm -p 5000:5000 [MODELNAME]:[TAG]
seldon-core-tester contract.json 0.0.0.0 5000 -p

# Add the image to your docker hub, ADD image to seldon deployment file(in this case canary.json) to deploy to seldon (eg. image: yourhubusername/[MODELNAME]:[TAG])
docker image ls
docker tag [IMAGE NUMBER] yourhubusername/[MODELNAME]:[TAG]
docker login --username=yourhubusername
docker push yourhubusername/[MODELNAME]:[TAG]
```

## Conclusions
