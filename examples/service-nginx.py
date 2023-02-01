from kubernetes import client, config
config.load_kube_config()

# Create a Service object
service = client.CoreV1Api().create_namespaced_service(
    namespace="bharat",
    body={
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {
            "name": "nginx-service"
        },
        "spec": {
            "type": "LoadBalancer",
            "ports": [{
                "port": 80,
                "targetPort": 80
            }],
            "selector": {
                "app": "nginx"
            }
        }
    }
)
service = client.CoreV1Api().read_namespaced_service
# Print the service details
# print(f"Service created: {service.metadata.name}")
print(f"Service DNS name: {service.status.load_balancer}")
