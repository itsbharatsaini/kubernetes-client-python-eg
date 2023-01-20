import time
from kubernetes import client, config
config.load_kube_config()
# k8s_api_client = client.ApiClient()
k8s_app_client = client.AppsV1Api()


# Create a Deployment object
deployment = k8s_app_client.create_namespaced_deployment(
    namespace="bharat",
    body={
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": "nginx-deployment"
        },
        "spec": {
            "replicas": 2,
            "selector": {
                "matchLabels": {
                    "app": "nginx"
                }
            },
            "template": {
                "metadata": {
                    "labels": {
                        "app": "nginx"
                    }
                },
                "spec": {
                    "containers": [{
                        "name": "nginx",
                        "image": "nginx:latest",
                        "ports": [{
                            "containerPort": 80
                        }]
                    }]
                }
            }
        }
    }
)

time.sleep(10)
result  = k8s_app_client.read_namespaced_deployment_status(deployment.metadata.name,deployment.metadata.namespace)
# Print the deployment status
print(f"Deployment status: {result.status.ready_replicas} out of {result.status.replicas} replicas are ready")