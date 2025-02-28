import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from utils.port_services import get_service_name

def tcp_scan(ip, ports, max_threads=100):
    results = {}
    
    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((str(ip), port))
                if result == 0:
                    results[port] = "Open"
                    service = get_service_name(port)
                    tqdm.write(f"Porta {port}: Open - {service}")
                elif result == 111: #RFC 793
                    results[port] = "Closed"
                    tqdm.write(f"Porta {port}: Closed")
                else:
                    results[port] = "Filtered"
                    tqdm.write(f"Porta {port}: Filtered")
        except Exception:
            results[port] = "Filtered"
            tqdm.write(f"Porta {port}: Filtered")
    
    try:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            list(tqdm(executor.map(scan_port, ports), total=len(ports), desc="Escaneando TCP"))
    except KeyboardInterrupt:
        print("\nEscaneamento TCP interrompido")
    
    return results