# MonitML

This repository contains the required files and write-up for Jason Lee's 2020 Insight DevOps project.

## Table of Contents
  - [1.0 Introduction](README.md#introduction)
  - [2.0 Tech stack](README.md#tech-stack)
  - [3.0 Demo](README.md#demo)
  - [4.0 Engineering Challenges](README.md#build-instructions)
  - [5.0 Conclusions](README.md#conclusions)

## Introduction
Machine Learning models can often have poor performance in production. Possible reasons of poor performing models in production may be attributed to differences between the data(features) used to train the models in development and the data(features) used to serve predictions in production. Furthermore, the model may have been trained on a data set that is completely different to what is found in production, reducing the predictive performance of the model. One other scenario that is possible is that the deployed model worked well in the past but has degraded over time due to changes in the environment. The world is not a static environment and for some use cases, ML models may need to be continuously retrained on newer data to have good predictive performance. In addition operational errors in production may occur due to "buggy" models or something as simple as accidently deploying the wrong model version. All of the described operational and predictive performance faults can decrease the business value of a ML service. To help reduce the time of finding errors in ML models in production as described above, I have created a tech stack in which the operational and predictive performance of machine learning models can be monitored in real-time.  


## Tech Stack
### Overview
![Fig 1: ML monitoring tech stack](/Images/techstack.PNG)
### Infrastructure as code: Terraform
### Configuration Management: Helm and Kustomize
### Model Training: KubeFlow
### Model Serving: Seldon Core 
### Monitoring/Alerting: Prometheus and Grafana
- Name
- Description
- Installation instructions
- Usage instructions
- Support instructions
- Contributing instructions
- Licence

Feel free to remove any sections that aren't applicable to your project.

## Demo
![Fig 2: Dashboard](/Images/dashboard.PNG)
![Fig 3: Alerting](/Images/alert.PNG)
## Build Instructions
```sh
curl -LO http://git.io/Xy0Chg
git add README.md
git commit -m "Use README Boilerplate"
```



## Conclusions
