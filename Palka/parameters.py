class Cli_Arguments():
    def __init__(self):
        import argparse
        import textwrap
        self.y_start = 0
        self.x_start = 0
        self.width = 50
        self.height = 50

        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description=textwrap.dedent('''\
        Palka
            Window positioning in Ubuntu
        '''))
        parser.add_argument('--xoffset', type=int, default=0, help='Percentage where the left border of the window should be on the screen. Value 0(left) to 100(right) defaults to 0')
        parser.add_argument('--yoffset', type=int, default=0, help='Percentage where the top border of the window should be on the screen. Value 0(top) to 100(bottom) defaults to 0')
        parser.add_argument('--width', type=int, help='Width of the window in percentages. Use negative percentages to flip it arround. Value -100 to 100 defaults to 50')
        parser.add_argument('--height', type=int, help='Height of the window in percentages. Use negative percentages to flip it arround. Value -100 to 100 defaults to 50')
        parser.add_argument('--install', type=bool, help='Incomplete, will setup the hotkeys')
        #todo add a window ID param.

        self.rawargs = parser.parse_args()

    def run_install(self):
        if self.rawargs.install:
            return True
        else:
            return False

    def validate_coordinates(self):
        if self.valid_percentage(self.rawargs.xoffset):
            self.x_start = self.rawargs.xoffset
        if self.valid_percentage(self.rawargs.yoffset):
            self.y_start = self.rawargs.yoffset
        if self.valid_percentage(self.rawargs.width):
            self.width = self.rawargs.width
        if self.valid_percentage(self.rawargs.height):
            self.height = self.rawargs.height

    def valid_percentage(self, number):
        if isinstance(number, int) and number <= 100:
            return True
        else:
            return False
