FROM python:3.10

COPY .devcontainer/requirements.txt requirements.txt 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY trigger_kubeflow_pipeline_vertex.py trigger_kubeflow_pipeline_vertex.py

# gcloud builds submit -t europe-north1-docker.pkg.dev/johan-kubeflow/docker-test/test

CMD ["python","trigger_kubeflow_pipeline_vertex.py"]