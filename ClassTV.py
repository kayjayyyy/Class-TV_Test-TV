# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 6 - Class TV_Test TV

class TV:
    # Parameterized constructor
    def __init__(self, channel, volume, power):
        self.getchannel = channel
        self.getvolume = volume
        self.TVpower = power
    
    # TV power setup, turn on and off
    def turnOn(self):
        self.TVpower = True

    def turnOff(self):
        self.TVpower = False

    # Getting channel
    def getChannel(self):
        if self.getchannel > 120:
            self.getchannel = 120
        elif self.getchannel < 1:
            self.getchannel = 1
        return self.getchannel
    
    # Getting volume
    def getVolume(self):
        if self.getvolume > 7:
            self.getvolume = 7
        elif self.getvolume < 1:
            self.getvolume = 1
        return self.getvolume
    
    # Channel setup; up and down
    def channelUp(self):
        if self.getchannel <= 119:
            self.getchannel = self.getchannel + 1

    def channelDown(self):
        if self.getchannel >= 2:
            self.getchannel = self.getchannel - 1
    
    # Volume setup; up and down
    def volumeUp(self):
        if self.getvolume <= 6:
            self.getvolume = self.getvolume + 1

    def volumeDown(self):
        if self.getvolume >= 2:
            self.getvolume = self.getvolume - 1