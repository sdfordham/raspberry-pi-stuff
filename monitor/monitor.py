import time
import psutil

from prometheus_client import start_http_server, Gauge


CPU_USAGE = Gauge("cpu_usage", "CPU", ["label"])
TEMPERATURE = Gauge("temp", "Temperature", ["label"])
MEMORY = Gauge("memory", "Memory", ["device", "mountpoint", "label"])
NETWORK = Gauge("network_io", "Network", ["interface", "label"])


def update_cpu():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    n = len(cpu_percent)
    cpu_dict = {f"cpu_{i + 1}": j for i, j in zip(range(n), cpu_percent)}
    for k, v in cpu_dict.items():
        CPU_USAGE.labels(label=k).set(v)

def update_temp():
    temps = psutil.sensors_temperatures()
    if "cpu_thermal" in temps and temps["cpu_thermal"]:
        cpu_thermal = temps["cpu_thermal"][0]
        for k, v in cpu_thermal._asdict().items():
            if isinstance(v, (int, float)):
                TEMPERATURE.labels(label=k).set(v)

def update_memory():
    partitions = psutil.disk_partitions()
    for p in partitions:
        memory_info = psutil.disk_usage(p.mountpoint)._asdict()
        for k, v in memory_info.items():
            if isinstance(v, (int, float)):
                MEMORY.labels(device=p.device, mountpoint=p.mountpoint, label=k).set(v)

def update_network():
    net_io = psutil.net_io_counters(pernic=True)
    for k, v in net_io.items():
        for kk, vv in v._asdict().items():
            if isinstance(vv, (int, float)):
                NETWORK.labels(interface=k, label=kk).set(vv)


if __name__ == "__main__":
    start_http_server(55555)
    while True:
        update_cpu()
        update_temp()
        update_memory()
        update_network()
        time.sleep(15)
