from os import path
from kubernetes import client, config, utils

NAMESPACE = "bharat"
yaml_file_path = "yaml-files\\nginx\\nginx-deployment.yaml"
# yaml_file_path = "<Your_Yaml_File_Path>"

def main():
    config.load_kube_config()
    k8s_api_client = client.ApiClient()
    k8s_app_client = client.AppsV1Api()

    try:
        deploymentName = yaml_file_path.split("\\")[-1].split(".")[0]
        utils.create_from_yaml(k8s_api_client,yaml_file_path,namespace=NAMESPACE)
        restult  = k8s_app_client.read_namespaced_deployment_status(deploymentName, NAMESPACE)
        print("'{0}' created successfully !!".format(restult.metadata.name))
    except:
        print("!!ERROR - '" + deploymentName + "' failed!!")

if __name__ == '__main__':
    main()