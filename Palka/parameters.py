class Cli_Arguments():
    def __init__(self):
        import argparse
        self.y_start = 0
        self.x_start = 0
        self.width = 50
        self.height = 50

        parser = argparse.ArgumentParser(description='Window placement by cli script')
        parser.add_argument('--xoffset', type=int, help='X placement percentage 0 it left -0 is right')
        parser.add_argument('--yoffset', type=int, help='Y placement percentage 0 it top -0 is top')
        parser.add_argument('--width', type=int, help='Width of the window. Use negative to go back from the X point')
        parser.add_argument('--height', type=int, help='Height of the window. Use negative to go back from the Y point')
        parser.add_argument('--install', type=bool, help='Y placement percentage 0 it top -0 is top')

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
