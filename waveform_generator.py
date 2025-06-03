class WaveformGenerator:
    def __init__(self, interface, resource_id):
        self.interface = interface
        self.resource_id = resource_id
        self.device = self.interface.connect(resource_id)

    def identify(self):
        return self.interface.send(self.resource_id, "*IDN?")

    def set_waveform(self, waveform_type="SIN"):
        self.interface.write(self.resource_id, f"FUNC {waveform_type}")

    def set_frequency(self, frequency):
        self.interface.write(self.resource_id, f"FREQ {frequency}")

    def set_amplitude(self, amplitude):
        self.interface.write(self.resource_id, f"VOLT {amplitude}")

    def output_on(self):
        self.interface.write(self.resource_id, "OUTP ON")

    def output_off(self):
        self.interface.write(self.resource_id, "OUTP OFF")
