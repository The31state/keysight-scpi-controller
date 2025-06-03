import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

print("\nDiscovered VISA Instruments:")
for res in resources:
    try:
        inst = rm.open_resource(res)
        idn = inst.query("*IDN?").strip()
        print(f"{res} -> {idn}")
        inst.close()
    except Exception as e:
        print(f"{res} -> Error: {e}")
