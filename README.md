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

<i><b>Note:</b></i> You should grant your created service principal <i>Contributor</i> access to your target AML workspace.

## Getting Started

The guided walkthrough below highlights how to deploy and trigger an Azure Machine Learning pipeline via a CI pipeline in Azure DevOps. This AML pipeline executes an R script which leverages the AML SDK for R and which connects to a workspace via Service Principal Authentication. 

It is recommended to first fork this repo, and then run the attached pipelines <i>as-is</i> before attempting to edit the underlying R scripts. Successful execution will validate that all connections can be made and that the remotely execute AML pipeline can authenticate to the workspace as expected.

- [Step 1 - Create Azure DevOps Service Connection to Machine Learning Workspace](#step-1---create-azure-devops-service-connection-to-machine-learning-workspace)
 - [Step 2 - Populate Azure Key Vault with AML Workspace & Service Principal Values](#step-2---populate-azure-key-vault-with-aml-workspace--service-principal-values)
 - [Step 3 - Create Key Vault-Linked Variable Group in Azure DevOps](#step-3---create-key-vault-linked-variable-group-in-azure-devops)
 - [Step 4 - Configure and Run your Continuous Integration Pipeline in Azure DevOps](#step-4---configure-and-run-your-continuous-integration-pipeline-in-azure-devops)
 - [Step 5 - Review Azure Machine Learning Pipeline Execution in Workspace](#step-5---review-azure-machine-learning-pipeline-execution-in-workspace)
 - [Step 6 - Integrate Custom R Code](#step-6---integrate-custom-r-code)

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

* From your Azure DevOps project, navigate to the expandable Pipelines menu and select <i>Library</i> and click the <i>+ Variable group</i> button.

![New Variable Group](doc_img/08.png?raw=true "New Variable Group")

* Name your new variable group `aml_kv_rg` and toggle the <i>Link secrets from an Azure key vault as variables</i> switch to on. When prompted select the Azure subscription and key vault you have added your secrets to.

![Variable Group Definition](doc_img/09.png?raw=true "Variable Group Definition")

* Under the variables panel click `+ Add` and select the five secrets you added to your key vault. Once completed click <i>Save</i>.

![Variable Group Variables](doc_img/10.png?raw=true "Variable Group Variables")

## Step 4 - Configure and Run your Continuous Integration Pipeline in Azure DevOps

* From your Azure DevOps project, navigate to pipelines and click <i>New Pipeline</i>. When prompted to connect your code select the <i> GitHub YAML</i> option.

![GitHub YAML](doc_img/11.png?raw=true "GitHub YAML")

* When prompted to select a repository navigate to your fork of this repo.

![GitHub MLOps Repo](doc_img/12.png?raw=true "GitHub MLOps Repo")

* When asked to configure your pipeline select the <i>Existing Azure Pipelines YAML file</i> option.

![Existing YAML](doc_img/13.png?raw=true "Existing YAML")

* Select the file at `/.pipelines/publish_aml_pipeline.yml` from the main branch of the repo then click <i>Continue</i>.

![Pipeline YAML](doc_img/14.png?raw=true "Pipeline YAML")

* From the pipeline review panel click <i>Run</i>. This will trigger a CI pipeline execution, upon successful completion your pipeline stages should appear similar to what is shown below.

![Pipeline Status](doc_img/15.png?raw=true "Pipeline Status")

## Step 5 - Review Azure Machine Learning Pipeline Execution in Workspace

* Navigate to your target Azure Machine Learning workspace. Select <i>Pipelines</i> from the sidebar menu and navigate to the <i>Pipeline endpoints</i> tab. You should see a published pipeline endpoint with the name `r_pipeline`. Note: this is the default pipeline name that can be overridden by updating the values in the `.pipelines/variable_template.yml` file.

![Published Pipeline Endpoint](doc_img/16.png?raw=true "Published Pipeline Endpoint")

* Navigate to the experiments tab. The Azure DevOps pipeline should have executed an experiment called `mlops_pipeline_run`. Once again, this value can be overridden by replacing the values in the `.pipelines/variable_template.yml` file. If successful this pipeline execution should reflect completion of a single step called <i>Run R Script</i>.

![Published Pipeline Endpoint](doc_img/17.png?raw=true "Published Pipeline Endpoint")

## Step 6 - Integrate Custom R Code

* At this point you have tested and validated that all connections in Azure have been made correctly and that you can successfully execute an R script remotely inside of AML - nice work! You can customize the environment that your R script runs in by modifying the Dockerfile definition at `azure_ml/python/Dockerfile`. Also, you can update the executed R script by placing a new R script inside the `azure_ml/R` directory - be sure to modify the name of the `R_SCRIPT` variable inside `.pipelines/variable_template`.