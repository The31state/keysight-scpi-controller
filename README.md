# keysight-scpi-controller
# Keysight SCPI Controller

This Python project provides a structured and extensible platform to interface with a wide range of Keysight equipment using SCPI commands. The project supports instruments such as:

- Oscilloscopes
- DC Power Supplies
- Digital Multimeters (DMMs)
- Waveform Generators

## Features
- Modular design with dedicated modules per instrument
- SCPI command logging to track device communication
- Device-specific functions like setting voltage, waveform configuration, channel toggling, and measurements
- Auto-connection using VISA resource identifiers
- CLI control for fast command-line interaction
- Auto-detection of VISA instruments
- CSV and SQLite logging of measurements
- Flask-based web interface (planned)

## Setup
```bash
pip install -r requirements.txt
```

## Run Example
```bash
python main.py
```

## Run CLI
```bash
python cli.py --device scope --action identify
python cli.py --device dcpower --channel 1 --voltage 3.3 --action set_voltage
```

## Run Auto-Detection
```bash
python discover.py
```

## Roadmap
- [x] Modular Instrument Support
- [x] Logging to text file
- [x] CLI Interface with argparse
- [x] Auto-detect VISA resources
- [x] CSV logging of measurements
- [x] SQLite logging of measurements
- [ ] Flask-based remote control GUI
- [ ] Optional PyQt desktop interface
