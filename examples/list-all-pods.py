from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

k8s_core_api = client.CoreV1Api()

result = k8s_core_api.list_pod_for_all_namespaces()
print("Listing pods with their IPs:")
for i in result.items:
    print("%s\t\t%s" % (i.metadata.namespace, i.metadata.name))