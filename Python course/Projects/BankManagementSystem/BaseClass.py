from abc import ABC

class Base(ABC):

    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address
        