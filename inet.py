import psutil
import time
from termcolor import colored

def main():
    while True:
        print("============================================")  # Separation line added here
        net_stats = {}

        for conn in psutil.net_connections(kind='inet'):
            try:
                local_port = conn.laddr.port if hasattr(conn.laddr, 'port') else conn.laddr[1]
                remote_port = conn.raddr.port if hasattr(conn.raddr, 'port') else conn.raddr[1] if conn.raddr else None

                pid = conn.pid
                if pid:
                    if pid not in net_stats:
                        p = psutil.Process(pid)
                        net_stats[pid] = {'name': p.name(), 'sent': 0, 'received': 0}

                    net_stats[pid]['sent'] += 100  # Replace with real sent data
                    net_stats[pid]['received'] += 50  # Replace with real received data
            except Exception as e:
                print(f"An error occurred: {e}")

        sorted_stats = sorted(net_stats.values(), key=lambda k: k['sent'], reverse=True)[:10]

        for idx, stat in enumerate(sorted_stats, 1):
            rank = f"{idx}º"
            sent_str = colored(f"{stat['sent']} bytes", 'red') if stat['sent'] > 0 else f"{stat['sent']} bytes"
            received_str = colored(f"{stat['received']} bytes", 'green') if stat['received'] > 0 else f"{stat['received']} bytes"
            
            print(f"{rank} Process: {stat['name']}, Sent: {sent_str}, Received: {received_str}")

        time.sleep(2)  # Set the sleep time for the refresh rate

if __name__ == '__main__':
    main()

