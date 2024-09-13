from prometheus_client import Counter, Gauge, generate_latest
import psutil

request_counter = Counter('Request_Counter', 'Count number of request')
cpu_usage = Gauge('cpu_usage', 'Get current cpu usage')
ram_usage = Gauge('ram_usage', 'Get current ram usage')
storage_usage = Gauge('storage_usage', 'Get current storage usage')

def generate_data():
    cpu_usage.set(psutil.cpu_percent())
    ram_usage.set(psutil.virtual_memory().percent)
    storage_usage.set(psutil.disk_usage('/').percent)
    return generate_latest()