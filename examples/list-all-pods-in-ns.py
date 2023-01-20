from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
k8s_core_api = client.CoreV1Api()

NAMESPACE = "bharat"
result = k8s_core_api.list_pod_for_all_namespaces()

print("Listing all pods in '" + NAMESPACE + "' Namespace")
for i in result.items:
    if i.metadata.namespace == NAMESPACE:
        print(i.metadata.name)