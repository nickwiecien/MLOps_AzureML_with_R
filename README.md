# MLOps: Azure ML using R

This repo contains a continuous integration (CI) pipeline to be run from Azure DevOps that completes two activities:
* Build and publish an Azure ML pipeline that executes an R script using a custom environment
* Triggers execution of the Azure ML pipeline and awaits completion

The pipelines in this repo are adapted from Microsoft's [MLOpsForPython Template Repository](https://github.com/microsoft/MLOpsPython/blob/master/docs/getting_started.md#create-a-variable-group-for-your-pipeline).

## Required Azure Resources
To execute the pipelines in this repository you will need to have access to the following Azure resources:
* Azure Machine Learning Workspace
* Azure Key Vault
* Azure DevOps Project
* Service Principal

## Getting Started

The guided walkthrough below highlights how to deploy and trigger an Azure Machine Learning pipeline via a CI pipeline in Azure DevOps. This AML pipeline executes an R script which leverages the AML SDK for R and which connects to a workspace via Service Principal Authentication.

## Step 1 - Create Azure DevOps Service Connection to Machine Learning Workspace

From your Azure DevOps project, create a new service connection to your target Azure Machine Learning Workspace.

* Navigate to Project Settings, then to Service Connections, and click <i>New service connection</i>.

![Service Connections](doc_img/01.png?raw=true "Service Connections")

* Select Azure Resource Manager then click <i>Next</i>.

![Azure Resource Manager](doc_img/02.png?raw=true "Azure Resource Manager")

* Leave Service principal (automatic) selected and click <i>Next</i>.

![Service Principal Automatic](doc_img/03.png?raw=true "Service Principal Automatic")

* Under Scope level, select <i>Machine Learning Workspace</i>, then choose the appropriate subscription, resource group, and AML resource. Name your service connection `aml-workspace-connection`. Finally, under security, check <i>Grant access permission to all pipelines</i> then click <i>Save</i>.  

![AML Workspace Connection](doc_img/04.png?raw=true "AML Workspace Connection")