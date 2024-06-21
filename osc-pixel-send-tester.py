"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import math
import random
import time

from pythonosc import udp_client

TOTAL_NUMBER_OF_PIXELS = 192

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", required=True, help="The ip of the OSC server")
    parser.add_argument(
        "--port",
        type=int,
        required=True,
        help="The port the OSC server is listening on",
    )
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        out = f"{r:02X}{g:02X}{b:02X}" * TOTAL_NUMBER_OF_PIXELS
        # print("len(out)", len(out))
        client.send_message("/leds", out)
        time.sleep(0.0001)
        # print("sent")
