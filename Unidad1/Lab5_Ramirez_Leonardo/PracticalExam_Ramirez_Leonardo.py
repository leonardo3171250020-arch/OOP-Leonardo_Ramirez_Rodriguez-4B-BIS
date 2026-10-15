class Device:
    def __init__(self,mac_add,type):
        self.mac_address=mac_add
        self.type=type
        self.bandwith=100
        self.networks=[]

    def register_router(self,router):
        self.networks.append(router)

    def connect_network(self):
        ssid=input("introduce the ssid of the router: ")
        password=input("Introduce the password of the network: ")
        for i in self.networks:
            if ssid == i.ssid:
                if password == i._password:
                    print ("Connection succesful")
                    i.register_device(self)
                    break
        else:
            print ("Network not found")

    def limit(self):
        restriction=int(input("Introduce how many mbps you want to limit this device to: "))
        self.bandwith=restriction

    def free(self):
        self.bandwith=100


class Router:
    def __init__(self,ssid,password):
        self.ssid=ssid
        self.devices=[]
        self._password=password

    def register_device(self,device):
        self.devices.append(device)

    def show_mbps(self):
        total_mbps=0
        for i in self.devices:
            total_mbps+=i.bandwith
        print(total_mbps)

device1=Device("1234.1234.1234","Smartphone")
device2=Device("ABCD.ABCD.ABCD","Laptop")

router1=Router("Network1","12345678")

device1.register_router(router1)
device1.connect_network()
device2.register_router(router1)
device2.connect_network()
device2.limit()
router1.show_mbps()
        
        