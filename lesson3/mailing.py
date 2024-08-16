from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        if not isinstance(to_address, Address) or not isinstance(from_address, Address):
            raise TypeError("to_address and from_address must be of type Address")
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __repr__(self):
        return (f"Mailing(to_address={self.to_address}, "
                f"from_address={self.from_address}, "
                f"cost={self.cost}, track='{self.track}')")