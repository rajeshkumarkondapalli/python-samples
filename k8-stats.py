# pip install kopf
# pip install prometheus-api-client

from prometheus_api_client import PrometheusConnect
import kopf
import kubernetes

# Initialize the Kubernetes client
kubernetes.config.load_kube_config()

# Handler for the creation of a pod
@kopf.on.create('pods')
def on_create(spec, name, namespace, logger, **kwargs):
    logger.info(f"A pod named {name} was created in namespace {namespace}")

# Handler for updating a pod
@kopf.on.update('pods')
def on_update(spec, name, namespace, logger, **kwargs):
    logger.info(f"A pod named {name} was updated in namespace {namespace}")

# Handler for deleting a pod
@kopf.on.delete('pods')
def on_delete(spec, name, namespace, logger, **kwargs):
    logger.info(f"A pod named {name} was deleted from namespace {namespace}")

# Run the Kopf operator
if __name__ == '__main__':
    kopf.run()




# Connect to Prometheus
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

# Define the prefix
prefix = "your-prefix"  # Replace with your actual prefix

# Define the query
query = f'count(kube_pod_info{{pod=~"{prefix}.*"}})'

# Fetch metrics
number_of_pods = prom.custom_query(query=query)

# Extract the count from the query result
pod_count = int(number_of_pods[0]['value'][1])

print(f"Number of pods starting with '{prefix}': {pod_count}")
