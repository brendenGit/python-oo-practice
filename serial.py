"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        On creation of a new SerialGenerator instance the instance will create a start, a serial, and a count

        start: holds starting value 
        serial: holds unique serial numbers
        count: checks for first occurance of generation
        """
        self.start = start
        self.serial = self.start
        self.count = 0

    def __repr__(self) -> str:
        return f"<SerialGenerator start={self.start} next={self.serial + 1}>"

    def generate(self):
        """SerialGenerator method for generating new serial number"""
        if self.count == 0:
            self.count += 1
            return self.serial
        elif self.count != 0:
            self.serial = self.serial + 1
            return self.serial

    def reset(self):
        """SerialGenerator method for reseting serial to original start value"""
        self.serial = self.start
        self.count = 0