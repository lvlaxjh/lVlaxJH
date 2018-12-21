import socket
if "__main__" == __name__:

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print("create socket succ!");

        sock.bind(('localhost', 8001));
        print("bind socket succ!");

        sock.listen(5);
        print("listen succ!");

    except:
        print("init socket err!");

    while True:
        print("listen for client...");
        conn, addr = sock.accept();
        print("get client");
        print(addr);

        conn.settimeout(5);
        szBuf = conn.recv(1024);
        print("recv:" + (str)(szBuf));

        if "0" == szBuf:
            conn.send(bytes('exit', encoding = "utf8"));
        else:
            conn.send(bytes('welcome', encoding = "utf8"));

        conn.close();
        print("end of sevice");