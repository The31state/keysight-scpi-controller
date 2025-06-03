class DCPower:
    def __init__(self, interface, resource_id):
        self.interface = interface
        self.resource_id = resource_id
        self.device = self.interface.connect(resource_id)

    def identify(self):
        return self.interface.send(self.resource_id, "*IDN?")

    def set_voltage(self, channel, voltage):
        self.interface.write(self.resource_id, f"INST:NSEL {channel}")
        self.interface.write(self.resource_id, f"VOLT {voltage}")

    def output_on(self, channel):
        self.interface.write(self.resource_id, f"INST:NSEL {channel}")
        self.interface.write(self.resource_id, "OUTP ON")

    def output_off(self, channel):
        self.interface.write(self.resource_id, f"INST:NSEL {channel}")
        self.interface.write(self.resource_id, "OUTP OFF")
