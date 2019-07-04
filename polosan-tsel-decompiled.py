# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: dg
import os, sys, time, random, socket, select, datetime, threading
lock = threading.RLock()
os.system('cls' if os.name == 'nt' else ' ')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [ x for x in array if x ]


def colors(value):
    patterns = {'R1': '\x1b[31;1m', 
       'R2': '\x1b[36;2m', 'G1': '\x1b[32;1m', 
       'Y1': '\x1b[33;1m', 'P1': '\x1b[35;1m', 
       'CC': '\x1b[0m'}
    for code in patterns:
        value = value.replace(('[{}]').format(code), patterns[code])

    return value


def log(value, status='', color=''):
    value = colors(('{value}[CC]').format(time=datetime.datetime.now().strftime(''), value=value, color=color, status=status))
    with lock:
        print value


def log_replace(value, status='[ Rusmana-ID ]', color='[G1]'):
    value = colors(('{}{} ({})        [CC]\r').format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()


class inject(object):

    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()
        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[G1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = open(real_path('/___server__id___.py')).readlines()
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log('___server__id___.py tidk ada', color='[R1]')
                return
            self.log(('').format(self.inject_host, self.inject_port))
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(4096)
                domain_fronting(socket_client, frontend_domains).start()

        except Exception as exception:
            self.log(('').format(self.inject_host, self.inject_port), color='[R1]')


class domain_fronting(threading.Thread):

    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()
        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 9999
        self.daemon = True

    def log(self, value, status='FREE INTERNET INDONESIA', color='[G1]'):
        log(value, status=status, color=color)

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [
         socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors:
                break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data:
                            break
                        else:
                            if sock is socket_client:
                                socket_tunnel.sendall(data)
                            else:
                                if sock is socket_tunnel:
                                    socket_client.sendall(data)
                        timeout = 0
                    except:
                        break

            if timeout == 60:
                break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '443'
            self.log(('\x1b[39;1m[ \x1b[31;1mBELUM KONEK \x1b[39;1m]\x1b[32;1m@>\x1b[31;1m[ \x1b[35;1mStatus 404 No \x1b[31;1m]').format(self.proxy_host, self.proxy_port))
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall('HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            os.system('clear')
            os.system('\nsh ___bug_server__.sh')
            self.log(('\x1b[39;1m[ \x1b[32;1mSUDAH KONEK \x1b[39;1m]\x1b[32;1m@>\x1b[31;1m[ \x1b[36;1mStatus 200 OK \x1b[31;1m]\n\x1b[39;1mCONNECT [host_port] [protocol][crlf]Host: \nmy.telkomsel.info[crlf]X-Online-Host: \nmy.telkomsel.info[crlf]X-Forward-Host: \nmy.telkomsel.info[crlf]X-Forwarded-For: \nmy.telkomsel.info[crlf]Connection: Keep-Alive[crlf][crlf]').format(self.proxy_host, self.proxy_port), color='[R1]')
        except OSError:
            self.log('Connection error', color='[R1]')
        except TimeoutError:
            self.log(('{} not responding').format(self.proxy_host), color='[R1]')


def main():
    print colors(('\n').join([]))
    inject('127.1.1.8', '10011').start()


if __name__ == '__main__':
    main()