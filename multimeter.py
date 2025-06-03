class Multimeter:
    def __init__(self, interface, resource_id):
        self.interface = interface
        self.resource_id = resource_id
        self.device = self.interface.connect(resource_id)

    def identify(self):
        return self.interface.send(self.resource_id, "*IDN?")

    def read_voltage(self):
        return self.interface.send(self.resource_id, "MEAS:VOLT:DC?")

    def read_current(self):
        return self.interface.send(self.resource_id, "MEAS:CURR:DC?")

    def read_resistance(self):
        return self.interface.send(self.resource_id, "MEAS:RES?")
