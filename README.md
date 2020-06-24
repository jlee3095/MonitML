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
###Prerequisites
The following software must be installed into your local environment:
Terraform
Helm
AWS CLI
Kfctl
Kubectl



```sh
git clone -m "Use README Boilerplate"
```



## Conclusions
