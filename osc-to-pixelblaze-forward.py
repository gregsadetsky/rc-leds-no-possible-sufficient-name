# -------------
# 192 pixels total
# 58 pixel vertically on the left
# 77 pixels horizontal at the top
# 57 pixels vertical on the right
# -------------
# vertical center is around pixel index 97/98
# -------------

from pixelblaze import *
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

TOTAL_NUMBER_OF_PIXELS = 192

UDP_SERVER_LISTEN_ON_IP = "0.0.0.0"
UDP_SERVER_LISTEN_ON_PORT = 13000

# TODO could this be found otherwise / not hardcoded??
pb = Pixelblaze("10.100.6.233")

# see the "show-pixels-from-websockets.pixelblaze.js" file!
pb.setActivePatternByName("show-pixels-from-websockets")
# pb.setBrightnessSlider(0.01)


def osc_message_handler(addr, arg):
    print("osc_message_handler", "len(arg)", len(arg))
    assert type(arg) is str
    # each pixel is 3 hex chars e.g. FF for red, 00 for green, F0 for blue i.e. 6 chars per pixel
    assert len(arg) == (TOTAL_NUMBER_OF_PIXELS * 3 * 2)
    # print("osc_message_handler", "addr", addr, "arg", arg)
    pixel_values_out = []
    for pixel_index in range(TOTAL_NUMBER_OF_PIXELS):
        pixel_hex = arg[pixel_index * 6 : (pixel_index + 1) * 6]
        pixel_values_out += [int(pixel_hex[i : i + 2], 16) for i in (0, 2, 4)]
    # print("pixel_values_out", pixel_values_out)
    pb.setActiveVariables({"pixels": pixel_values_out})


dispatcher = Dispatcher()
dispatcher.map("/leds", osc_message_handler)

server = osc_server.ThreadingOSCUDPServer(
    (UDP_SERVER_LISTEN_ON_IP, UDP_SERVER_LISTEN_ON_PORT), dispatcher
)
print("Serving on {}".format(server.server_address))
server.serve_forever()
