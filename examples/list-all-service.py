from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
k8s_core_api = client.CoreV1Api()

namespaces = k8s_core_api.list_namespace()
print("Listing all Services :")
for ns in namespaces.items:
    NAMESPACE = ns.metadata.name
    result = k8s_core_api.list_namespaced_service(NAMESPACE)
    for i in result.items:
        print("%s\t\t%s\t\t%s" % (i.metadata.namespace, i.metadata.name, i.status.load_balancer))