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
# README Boilerplate

A template of README best practices to make your README simple to understand and easy to use. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Download to your project directory, add `README.md`, and commit:

```sh
curl -LO http://git.io/Xy0Chg
git add README.md
git commit -m "Use README Boilerplate"
```

## Usage

Replace the contents of `README.md` with your project's:

- Name
- Description
- Installation instructions
- Usage instructions
- Support instructions
- Contributing instructions
- Licence

Feel free to remove any sections that aren't applicable to your project.

## Support

Please [open an issue](https://github.com/fraction/readme-boilerplate/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).
