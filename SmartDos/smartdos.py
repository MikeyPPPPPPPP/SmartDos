 #made by michael provenzano (good year)
import packet
import useragent
import json
import threading
import requests
import interface
import socket
import time


####
#socket.gethostbyaddr("69.59.196.211")
#####

class send:
    def __init__(self, settings_file):
        self.settings_file = settings_file
        self.file = open(self.settings_file, "r")#opens file
        self.son = json.load(self.file)# loads data
        self.userAgent = {'User-agent':self.son["user_agent"]}
        self.port = self.son["port"]
        self.method = self.son["methoud"]
        self.url = self.son["url"]
        self.timeout = self.son["timeout"]
        self.data = self.son["data"]
        self.file.close()

    def bombs_away(self):
        if self.method == 'get' or 'GET':
            req = requests.get(self.url, headers = self.userAgent, timeout=self.timeout)
            print(req)
        if self.method == 'post' or 'POST':
            req = requests.get(self.url, headers = self.userAgent, timeout=self.timeout, data=self.data)

def builder():
    print(interface.print_stuff.banner())
    number_to_send = 0
    t = packet.packet()
    meth = input("GET or POST: ")
    t.methoud = meth
    print(interface.print_stuff.packet_builder())
    print("pick useragent")
    time.sleep(3)
    ua = useragent.agent()
    ua.options()
    ua.pick_option()
    ua.agentviewer()
    ua.pick_agent()

    t.user_agent = ua.agent
    por = input("port (default 443): ")
    t.port = por
    ur = input('url (if port 443 add https:// ): ')
    t.url = ur
    ti = input('Timeout: ')
    t.timeout = int(ti)
    da = input('Data if POST: ')
    t.data = ""
    t.build()
    
def craper(numb):
    pak = send('settings.json')
    for x in range(1,numb):
        pak = send('settings.json')
        pak.bombs_away()

def main():
    builder()
    numb = int(input("number of packets to send: "))
    threa = int(input("number of Threads: "))
    threads = []
    for i in range(threa):
        t = threading.Thread(target=craper, args=(numb,))
        threads.append(t)
        t.start()
    


if __name__ == '__main__':
    main()
#pak = send('settings.json')
#pak.bombs_away()

#t = interface.print_stuff.banner()
#print(t)




