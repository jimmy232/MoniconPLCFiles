from cellulariot import cellulariot
node = cellulariot.CellularIoT(serial_port="/dev/ttyUSB2", board="Sixfab Raspberry Pi Base HAT")

node.sendATComm("node.sendATComm("AT","OK\r\n")","\n")
