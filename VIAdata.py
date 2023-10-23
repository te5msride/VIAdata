import can


def receive_can_messages(channel, sensor_can_id):
    bus = can.interface.Bus(channel=channel, bustype="socketcan")
    while True:
        message = bus.recv()
        if message.arbitration_id == sensor_can_id:
            torque_data = parse_torque_data(message.data)
            print("Torque: ", torque_data)


def parse_torque_data(data):
    # You will need to implement this based on your sensor's documentation
    return converted_torque_value


if __name__ == "__main__":
    SENSOR_CAN_ID = 0x123  # Replace with your sensor’s CAN ID
    receive_can_messages("can0", SENSOR_CAN_ID)
