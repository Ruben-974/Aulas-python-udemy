class Client:

    def __init__(self, name='Anonymous'):
        self.name = name
        self.addresses = []

    def append_addresses(self, road=None, number=None):
        self.addresses.append(Address(road, number))

    def append_addresses_direct(self, add):
        self.addresses.append(add)

    def print_addresses(self):
        for ad in self.addresses:
            print(ad.road, ad.number)

    def __del__(self):
        print('Dell Client...')


class Address:

    def __init__(self, road, number):
        self.road = road
        self.number = number

    def __del__(self):
        print('Dell Address...')


client1 = Client('Rose')
client1.append_addresses('E', 41)


address = Address('B', 45)
client1.append_addresses_direct(address)

client1.print_addresses()


