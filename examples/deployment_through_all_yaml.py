import os
from kubernetes import client, config, utils

NAMESPACE = "bharat"
yaml_files_path = "D:\\Projects\\Kubernetes Python Client\\kubernetes-client-python-eg\\yaml-files\\nginx\\"
# yaml_files_path = "<Your_Yaml_File_Path>" +"\\"

# Collect all yaml files path in a list.
deployment_files = []
for entry in os.listdir(yaml_files_path):
    if os.path.isfile(os.path.join(yaml_files_path, entry)):
        deployment_files.append(entry)

#Deploy all yaml files.
def main():
    config.load_kube_config()
    k8s_api_client = client.ApiClient()
    k8s_app_client = client.AppsV1Api()

    for deploy in deployment_files:
        try:
            yaml_file_path = yaml_files_path + deploy
            
            deploymentName = yaml_file_path.split("\\")[-1].split(".")[0]
            print(deploymentName)
            utils.create_from_yaml(k8s_api_client,yaml_file_path,namespace=NAMESPACE)
            result  = k8s_app_client.read_namespaced_deployment_status(deploymentName, NAMESPACE)
            print("'{0}' created successfully !!".format(result.metadata.name))
        except:
            print("!!ERROR - '" + deploymentName + "' failed!!")

if __name__ == '__main__':
    main()