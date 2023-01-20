from kubernetes import client, config, watch

config.load_kube_config()
k8s_core_api = client.CoreV1Api()

result = k8s_core_api.list_namespace()

file = open("OUTPUT.json", "w")
file.write(str(result))
file.close()