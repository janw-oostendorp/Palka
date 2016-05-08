def installer():
    import subprocess

    wmctrl = subprocess.Popen(["which","wmctrl"], stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]

    # wmctrl installed?
    if not wmctrl:
        print("The program 'wmctrl' is currently not installed. Install with command `sudo apt-get install wmctrl`")
        return

    # get csv?

    # set defaults?

    # set hotkeys