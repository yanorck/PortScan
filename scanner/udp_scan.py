import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def udp_scan(ip, ports, max_threads=100):
    results = {}

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(0.5)
                s.sendto(b"", (str(ip), port))
                try:
                    data, _ = s.recvfrom(1024)
                    if data:
                        results[port] = "Open"
                        tqdm.write(f"Porta {port}: Open")
                except socket.timeout:
                    results[port] = "Open|Filtered"
                    tqdm.write(f"Porta {port}: Open|Filtered")
                except ConnectionResetError:
                    results[port] = "Closed"
                    tqdm.write(f"Porta {port}: Closed")
        except Exception as e:
            results[port] = "Filtered"
            tqdm.write(f"Porta {port}: Filtered (Erro: {e})")

    try:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            list(tqdm(executor.map(scan_port, ports), total=len(ports), desc="Escaneando UDP"))
    except KeyboardInterrupt:
        print("\nEscaneamento UDP interrompido")

    return results