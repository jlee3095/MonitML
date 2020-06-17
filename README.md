# MonitML

Setup
1) K8s Setup-> Terraform or EKSCTL
2a) Tech stack setup -> kctl install Kubeflow NOTE: Deleted SELDON from stack, Current version configured improperly, use helm install
2b) Tech stack -> Seldoncore Helm install
2c) Tech stack -> Seldoncore analytics install 
3) Creation of Models (Can skip this step, refined models are in repo)


DEMO
1) Deployment of Models -> Deploy good or bad model or both if can setup canary
2) conduct python script to add load to the inference server
3) Command to connect to grafana to observe the metrics
