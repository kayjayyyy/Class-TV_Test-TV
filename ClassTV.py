# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 6 - Class TV_Test TV

class TV:
    def __init__(self, channel, volume, power):
        # Parameretized constructor
        self.getchannel = channel
        self.getvolume = volume
        self.TVpower = power
        
    def turnOn(self):
        self.TVpower = True

    def turnOff(self):
        self.TVpower = False

    def getChannel(self):
        if self.getchannel > 120:
            self.getchannel = 120
        elif self.getchannel < 1:
            self.getchannel = 1
        return self.getchannel
    