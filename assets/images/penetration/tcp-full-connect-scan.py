#!/usr/bin/env python
import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def Scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect(host, port)
        conn.send('Test port')
        res = conn.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open '%port
        print '[+] ' + str(res)
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed'%port
    finally:
        screenLock.release()
        conn.close()

def portScan(host, ports):
    try:
        ip = gethostbyname(host)
    except:
        print "[-] Cannot resolev '%s': Unknown host"%host
        return
    try:
        name = gethostbyaddr(ip)
        print "[+] Scan results for: "+ name[0]
    except:
        print "[+] Scan results for: "+ ip
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=Scan, args=(host, int(port)))
        t.start()

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port[s]>')
    parser.add_option('-H', dest='host', type='string', help='specify target host')
    parser.add_option('-p', dest='ports', type='string', help='specify target port[s] separated by comma')

    (options, args) = parser.parse_args()
    host = options.host
    ports = str(options.ports).split(',')
    if (host == None) | (ports[0] == None):
        print parser.usage
        exit(0)
    portScan(host,ports)

if __name__ == '__main__':
    main()
