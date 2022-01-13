# MLOps - Azure ML using R

This repo contains a continuous integration (CI) pipeline to be run from Azure DevOps that completes two activities:
* Build and publish an Azure ML pipeline that executes an R script using a custom environment
* Triggers execution of the Azure ML pipeline and awaits completion.
The pipelines in this repo are adapted from Microsoft's [MLOpsForPython Template Repository](https://github.com/microsoft/MLOpsPython/blob/master/docs/getting_started.md#create-a-variable-group-for-your-pipeline) 