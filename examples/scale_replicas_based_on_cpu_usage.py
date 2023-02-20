from kubernetes import client, config
from prometheus_api_client import PrometheusConnect

searchQuery = 'pod_name:container_cpu_usage:sum{pod_name="php-apache-6df656f5cb-kf4hd"}'
# Prometheus
def cpu_usages(searchQuery) :
    # Prometheus Host URL
    prometheusUrl ="http://localhost:9090/"
    prom = PrometheusConnect(prometheusUrl, disable_ssl=True)
    prom.all_metrics()
    result = prom.custom_query(searchQuery)

    # query = result[0]['metric']['__name__']
    podName = result[0]['metric']['pod_name']
    value = float(result[0]['value'][-1][:5])
    return(podName, value)



#K8s
config.load_kube_config()
cpuUsages = cpu_usages(searchQuery)[-1]
podName = cpu_usages(searchQuery)[0]
thresholdValue = 0.1

NAMESPACE = "bharat"
deploymentName = "php-apache"


deployment = client.AppsV1Api().read_namespaced_deployment(deploymentName, NAMESPACE)
currentReplicas = deployment.spec.replicas



if cpuUsages >= thresholdValue :
    print('CPU usages of pod' + '"' + podName + '"' + 'reached threshold value')
    print(f"Scaling up replicas to : {currentReplicas + 1}")
    #Scale up the Deployment
    client.AppsV1Api().patch_namespaced_deployment(
        name=deploymentName,
        namespace=NAMESPACE,
        body={
            "spec": {
                "replicas": currentReplicas + 1
            }
        }
        )
else:
    if currentReplicas <= 1:
        pass
    else:
        print(f"Scaling down replicas to : {currentReplicas - 1}")
        #Scale down the Deployment
        client.AppsV1Api().patch_namespaced_deployment(
            name=deploymentName,
            namespace=NAMESPACE,
            body={
                "spec": {
                    "replicas": currentReplicas -1
                }
            }
            )