import psutil
import cpuinfo
import GPUtil

def get_sysinfo() -> str:
    cpu_info = cpuinfo.get_cpu_info()
    cpu = cpu_info["brand"] if "brand" in cpu_info else cpu_info["brand_raw"]
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    infostr = f"{cpu} {cores}c/{threads}t"
    try:
        gpus = GPUtil.getGPUs()
        infostr += f"\n{gpus[0].name}"
    except ValueError:
        pass
    return infostr

