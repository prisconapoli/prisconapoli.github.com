---
layout: post
category : Development
tags: [python, networking, port scanning]
image : penetration/security.png
tagline: Forging your own weapons to solve your own problems makes you a true penetration tester - TJ. O’Connor
---
{% include JB/setup %}

**A tcp full connect scanner in Python**

<!--more-->

Recently I read a wonderful book called [Violent Python](http://www.amazon.com/Violent-Python-Cookbook-Penetration-Engineers/dp/1597499579). The author  **TJ. O’Connor** is a Department of Defense expert in information security and a US army paratrooper. The book is easy to read, is full of useful tips and contains a short review of the most famous malwares or attacks made in the last 30 years. To be honest, the author pleasantly surprised me in showing how easily a penetration tester can build its own tools with Python.

Below is reported the full code of a tcp full scanned written in Python. It's nice to see that it suits in about 50 lines of code .

Download [tcp-full-connect-scan.py]({{ site.url }}/assets/images/penetration/tcp-full-connect-scan.py).

{% highlight python lineno%}
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


{% endhighlight %}


The program consists of three parts:

* Get the hostname and the list of ports. This can be accomplished using **optparse**, a powerful, extensible, and easy-to-use option parser. Use this library is extremely easy. All the work is done by three functions: **OptionParser()**,**add_option()**, and **parse_args()**
{% highlight python %}
parser = optparse.OptionParser('usage %prog -o <myoption>')
parser.add_option('-o', dest='myopt', type='string', help='specify a description for my_option')
(options, args) = parser.parse_args()
myopt = options.myopt
# use myopt
{% endhighlight %}
* To each port, start a new thread to create a socket and check if the port is open using the function **Scan**. To use **Thread** is required to provide function name that be called and the full list of argument:

{% highlight python %}
t = Thread(target=Scan, args=(host, int(port)))
t.start()
{% endhighlight %}    

* Create a connection using **socket**, a Python library that provides access to the BSD socket interface. 

{% highlight python %}
try:
    conn = socket(AF_INET, SOCK_STREAM)
    conn.connect(host, port)
finally:
    conn.close()
{% endhighlight %} 
     
Running the script on my MacBook I receive the following result:
{% highlight bash %}
root@2L:~# python ./tcp-full-connect-scan.py -H 127.0.0.1 -p 21,22,23,80
[+] Scan results for: localhost
[-]21/tcp open
[-]22/tcp closed
[-]23/tcp closed
[-]80/tcp closed
{% endhighlight %}


##Further Information
[socket](https://docs.python.org/2/library/socket.html), Low-level networking interface

[threading](https://docs.python.org/2/library/threading.html), Higher-level threading interface

[optparse](https://docs.python.org/2/library/optparse.html#module-optparse), Parser for command line options

[Violent Python](http://www.amazon.com/Violent-Python-Cookbook-Penetration-Engineers/dp/1597499579):  A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers, by TJ. O’Connor


