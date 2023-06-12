import qrcode
import socket


def search_for_nonlocalhost_ip(n) -> str:
    # port doesn't matter because it's theoretical anyway
    # format: [(address_family, udp_or_tcp, ?, ?, (address, port)), ...]
    info = socket.getaddrinfo(n, 8080)
    for i in info:
        if i[0] == socket.AddressFamily.AF_INET6:
            continue
        if i[4][0] == "127.0.0.1":
            continue
        return i[4][0]


def make_qr_to_path(path):
    hostname = socket.gethostname()
    ip = search_for_nonlocalhost_ip(hostname)

    img = qrcode.make("http://"+ip+":8000")
    img.save(path)
