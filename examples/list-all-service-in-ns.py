from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
k8s_core_api = client.CoreV1Api()

NAMESPACE = "bharat"

result = k8s_core_api.list_namespaced_service()
print("Listing Services :")
for i in result.items:
    print("%s\t%s" % (i.metadata.name, i.status.load_balancer))