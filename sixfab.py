from cellulariot import cellulariot
node = cellulariot.CellularIoT(serial_port="/dev/ttyUSB2", board="Sixfab Raspberry Pi Base HAT")

node.sendATComm("AT+CSQ","\n")
