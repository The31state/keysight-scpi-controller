import pyvisa
import logging

class SCPIInterface:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.connections = {}
        logging.basicConfig(filename='logs/session_log.txt', level=logging.INFO)

    def connect(self, resource_id):
        instrument = self.rm.open_resource(resource_id)
        self.connections[resource_id] = instrument
        logging.info(f"Connected to {resource_id}")
        return instrument

    def send(self, resource_id, command):
        if resource_id not in self.connections:
            raise Exception("Not connected to resource")
        response = self.connections[resource_id].query(command)
        logging.info(f"{resource_id} << {command} | >> {response.strip()}")
        return response.strip()

    def write(self, resource_id, command):
        if resource_id not in self.connections:
            raise Exception("Not connected to resource")
        self.connections[resource_id].write(command)
        logging.info(f"{resource_id} << {command}")

    def close_all(self):
        for conn in self.connections.values():
            conn.close()
        logging.info("Closed all connections")
