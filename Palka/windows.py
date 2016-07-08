def get_current_window():
    import subprocess
    import re
    current_window_id = get_current_window_id()

    xwininfo = subprocess.Popen(
        ['xwininfo', '-id', current_window_id],
        universal_newlines=True,
        stdout=subprocess.PIPE
    ).communicate()[0]

    dimensions = {
        "x": int(re.search("Absolute upper-left X:  ([0-9]+)", xwininfo).group(1)),
        "y": int(re.search("Absolute upper-left Y:  ([0-9]+)", xwininfo).group(1)),
        "width": int(re.search("Width: ([0-9]+)", xwininfo).group(1)),
        "height": int(re.search("Height: ([0-9]+)", xwininfo).group(1)),
    }
    window_object = Window(dimensions['x'], dimensions['y'], dimensions['width'], dimensions['height'])
    window_object.set_process_id(current_window_id)

    return window_object


def get_current_window_id():
    import subprocess
    import re

    xprop = subprocess.Popen(["xprop", '-root'], stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]

    # active_window_id = re.findall("connected (?:primary )?([0-9]+)x([0-9]+)\+([0-9]+)\+([0-9]+)", xprop)
    active_window = re.search("_NET_ACTIVE_WINDOW.*(0x.*)", xprop)
    return active_window.group(1)


def wmctrl(process_id, x, y, width, height):
    import subprocess

    coordinates = '0,' + ','.join([str(x), str(y), str(width), str(height)])

    subprocess.Popen(["wmctrl", '-ir', process_id, "-e", coordinates])


class Window:
    def __init__(self, x_start, y_start, width, height):
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.width = int(width)
        self.height = int(height)
        self.x_end = self.x_start + self.width
        self.y_end = self.y_start + self.height
        self.display = None
        self.process_id = None
        self.x_mid = round(self.width / 2)
        self.y_mid = round(self.height / 2)

    def set_process_id(self, process_id):
        self.process_id = process_id

    def get_process_id(self):
        return self.process_id

    def set_display(self, display):
        import Palka.displays as displays
        if type(display) is not displays.Display:
            raise ValueError('Invalid object type')

        self.display = display

    def get_display(self):
        return self.display

    def calc_target_dimensions(self, xoffset_percent, yoffset_percent, width_percent, height_percent):

        # combined percentages over 100%? Invert them
        if (xoffset_percent+width_percent) > 100:
            width_percent = -width_percent

        if (yoffset_percent + height_percent) > 100:
            height_percent = -height_percent

        # X offset
        absolute_x_offset = self.display.x_start + (round(self.display.width * (xoffset_percent / 100)))
        absolute_y_offset = self.display.y_start + (round(self.display.height * (yoffset_percent / 100)))
        absolute_width = (round(self.display.width * (abs(width_percent) / 100)))
        absolute_height = (round(self.display.height * (abs(height_percent) / 100)))

        if width_percent < 0:
            absolute_x_offset -= absolute_width

        if height_percent < 0:
            absolute_y_offset -= absolute_height

        return {
            'x': absolute_x_offset,
            'y': absolute_y_offset,
            'width': absolute_width,
            'height': absolute_height
        }
