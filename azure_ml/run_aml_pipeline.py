from azureml.pipeline.core import PublishedPipeline
from azureml.core import Experiment, Workspace
import argparse
import os


def main():

    parser = argparse.ArgumentParser("register")
    parser.add_argument(
        "--output_pipeline_id_file",
        type=str,
        default="pipeline_id.txt",
        help="Name of a file to write pipeline ID to"
    )
    parser.add_argument(
        "--skip_train_execution",
        action="store_true",
        help=("Do not trigger the execution. "
              "Use this in Azure DevOps when using a server job to trigger")
    )
    args = parser.parse_args()

    subscription_id = os.getenv("SUBSCRIPTION_ID")
    resource_group = os.getenv("RESOURCE_GROUP")
    workspace_name = os.getenv("WORKSPACE_NAME")
    workspace_region = os.getenv("WORKSPACE_REGION")

    pipeline_name = os.getenv("PIPELINE_NAME")
    build_id = os.getenv("BUILD_BUILDID")
    build_uri = os.getenv("BUILD_URI")
    experiment_name = os.getenv("EXPERIMENT_NAME")

    aml_workspace = Workspace.get(
        name=workspace_name,
        subscription_id=subscription_id,
        resource_group=resource_group
    )

    # Find the pipeline that was published by the specified build ID
    pipelines = PublishedPipeline.list(aml_workspace)
    matched_pipes = []

    for p in pipelines:
        if p.name == pipeline_name:
            if p.version ==build_id:
                matched_pipes.append(p)

    if(len(matched_pipes) > 1):
        published_pipeline = None
        raise Exception(f"Multiple active pipelines are published for build {build_id}.")  # NOQA: E501
    elif(len(matched_pipes) == 0):
        published_pipeline = None
        raise KeyError(f"Unable to find a published pipeline for this build {build_id}")  # NOQA: E501
    else:
        published_pipeline = matched_pipes[0]
        print("published pipeline id is", published_pipeline.id)

        # Save the Pipeline ID for other AzDO jobs after script is complete
        if args.output_pipeline_id_file is not None:
            with open(args.output_pipeline_id_file, "w") as out_file:
                out_file.write(published_pipeline.id)

        if(args.skip_train_execution is False):
            tags = {"BuildId": build_id}
            if (build_uri is not None):
                tags["BuildUri"] = build_uri
            experiment = Experiment(
                workspace=aml_workspace,
                name=experiment_name)
            run = experiment.submit(
                published_pipeline,
                tags=tags)

            print("Pipeline run initiated ", run.id)


if __name__ == "__main__":
    main()