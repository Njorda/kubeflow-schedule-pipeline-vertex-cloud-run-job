# This script sets up the connection to a Kubeflow Pipelines Artifact Registry
# using the RegistryClient from the kfp.registry module. It loads the necessary
# environment variables and establishes a connection to the registry.

import os
from kfp.registry import RegistryClient
from dotenv import load_dotenv
from google.cloud import aiplatform as aip

# Load environment variables from the .env file
load_dotenv()

# Retrieve required environment variables
gcp_project = os.getenv("gcp_project","johan-kubeflow")
kubeflow_pipelines_artifact_registyr = os.getenv('kubeflow_pipelines_artifact_registyr',"test-test")
package_name = 'ltv-train'
tag = 'latest'
bucket = 'gs://test-test-test-johan'

# Create a RegistryClient instance and connect to the Kubeflow Pipelines Artifact Registry
client = RegistryClient(host=f"https://europe-west1-kfp.pkg.dev/{gcp_project}/{kubeflow_pipelines_artifact_registyr}")

print(client.list_packages())

filename = client.download_pipeline(
  package_name = package_name,
  tag = tag,
  file_name = 'loca_file.yaml'
  )

job = aip.PipelineJob(
    #job_id='test' # TODO se in the future
    display_name="First kubeflow pipeline",
    template_path="loca_file.yaml",
    pipeline_root=bucket,
    location="europe-west1",
    project=gcp_project,
)

job.submit()