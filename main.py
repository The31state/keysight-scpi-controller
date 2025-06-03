from utils.scpi_interface import SCPIInterface
from instruments.oscilloscope import Oscilloscope
from instruments.dcpower import DCPower
from instruments.multimeter import Multimeter
from instruments.waveform_generator import WaveformGenerator

def main():
    interface = SCPIInterface()

    scope_id = "USB0::0x0957::0x1799::MY12345678::INSTR"
    dcpower_id = "USB0::0x2A8D::0x5302::MY12345789::INSTR"
    dmm_id = "USB0::0x0957::0x0607::MY12345890::INSTR"
    wavegen_id = "USB0::0x0957::0x0407::MY12345901::INSTR"

    try:
        scope = Oscilloscope(interface, scope_id)
        print("Oscilloscope:", scope.identify())
        scope.enable_channel(1)
        scope.autoscale()
        print("Voltage Measurement:", scope.measure_voltage(channel=1))

        power = DCPower(interface, dcpower_id)
        print("DC Power:", power.identify())
        power.set_voltage(channel=1, voltage=3.3)
        power.output_on(channel=1)

        dmm = Multimeter(interface, dmm_id)
        print("Multimeter:", dmm.identify())
        print("Voltage:", dmm.read_voltage())
        print("Current:", dmm.read_current())
        print("Resistance:", dmm.read_resistance())

        gen = WaveformGenerator(interface, wavegen_id)
        print("Waveform Generator:", gen.identify())
        gen.set_waveform("SIN")
        gen.set_frequency(1000)
        gen.set_amplitude(2.5)
        gen.output_on()

    except Exception as e:
        print("Error:", e)
    finally:
        interface.close_all()

if __name__ == "__main__":
    main()
