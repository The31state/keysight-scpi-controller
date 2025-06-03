class Oscilloscope:
    def __init__(self, interface, resource_id):
        self.interface = interface
        self.resource_id = resource_id
        self.device = self.interface.connect(resource_id)

    def identify(self):
        return self.interface.send(self.resource_id, "*IDN?")

    def autoscale(self):
        self.interface.write(self.resource_id, ":AUToscale")

    def measure_voltage(self, channel=1):
        return self.interface.send(self.resource_id, f":MEASure:VAMPlitude? CHANnel{channel}")

    def enable_channel(self, channel):
        self.interface.write(self.resource_id, f":CHANnel{channel}:DISPlay ON")

    def disable_channel(self, channel):
        self.interface.write(self.resource_id, f":CHANnel{channel}:DISPlay OFF")
