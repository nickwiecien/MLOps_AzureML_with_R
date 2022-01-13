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

<i><b>Note:</b></i> You should grant your created service principal <i>Contributor</i> access to your AML workspace.

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

## Step 2 - Populate Azure Key Vault with AML Workspace & Service Principal Values

* From the Azure portal, navigate to your target Key Vault and click <i>Secrets</i>. If you <u>do not</u> have permissions to view or create secrets in your Key Vault follow the steps below. First, navigate to <i>Access policies</i> along the left blade, click <i>+ Create</i>. From the Permissions tab, select <b>Get, List, and Set</b> under Secret Permissions and click <i>Next</i>. 

![Key Vault Permissions](doc_img/05.png?raw=true "Key Vault Permissions")

* Under the Principal tab, select your Active Directory account and click <i>Next</i>. Skip the optional application section and under Review + create click <i>Create</i>.

![Access Policy Create](doc_img/06.png?raw=true "Access Policy Create")

* Navigate to the <i>Secrets</i> tab along the left blade and create 5 new secrets with the values listed in the table below.

| Secret Name | Secret Value |
|-------------|--------------|
|RESOURCE-GROUP|Name of the resource group which contains your target AML workspace|
|WORKSPACE-NAME|Name of your target AML workspace|
|TENANT-ID|Tenant ID associated with your service principal. Listed as `Directory (tenant) ID` in the service principal overview tab|
|SERVICE-PRINCIPAL-ID|Client ID of the service principal.  Listed as  `Application (client) ID` in the service principal overview tab|
|SERVICE-PRINCIPAL-SECRET|Secret value associated with your service principal|

![Key Vault Secrets](doc_img/07.png?raw=true "Key Vault Secrets")

## Step 3 - Create Key Vault-Linked Variable Group in Azure DevOps

*