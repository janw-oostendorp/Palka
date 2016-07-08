def get_displays():
    import subprocess
    import re

    xrandr = subprocess.Popen("xrandr", stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]

    screens_resolutions = re.findall("connected (?:primary )?([0-9]+)x([0-9]+)\+([0-9]+)\+([0-9]+)", xrandr)

    displays = list()
    for details in screens_resolutions:
        displays.append(
            Display(details[2], details[3], details[0], details[1])
        )

    return displays


class Display:
    def __init__(self, x_start, y_start, width, height):
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.width = int(width)
        self.height = int(height)
        self.x_end = self.x_start + self.width
        self.y_end = self.y_start + self.height

    def window_in_screen(self, window):
        import Palka.windows as windows

        if type(window) is not windows.Window:
            raise ValueError('Invalid object type')

        # X-axis?
        x_valid = False
        # window within X offset?
        if self.x_start <= (window.x_start+window.x_mid) <= self.x_end:
            x_valid = True

        # Y-axis?
        y_valid = False
        # windows top within the top and bottom of given screen
        if self.y_start <= (window.y_start+window.y_mid) <= self.y_end:
            y_valid = True

        if x_valid and y_valid:
            return True

        return False
