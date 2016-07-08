from Palka.parameters import Cli_Arguments

args = Cli_Arguments()

if args.run_install():
    import Palka.install as install

    print('@todo install')
    install.installer()
else:
    import Palka.displays as displays
    import Palka.windows as windows

    displays_objects = displays.get_displays()
    obj_window = windows.get_current_window()

    args.validate_coordinates()

    for display_obj in displays_objects:
        if not display_obj.window_in_screen(obj_window):
            continue

        obj_window.set_display(display_obj)
        target_pixels = obj_window.calc_target_dimensions(args.x_start, args.y_start, args.width, args.height)

        print("target coordinates and dimension of the window")
        print(target_pixels)

        windows.wmctrl(
            obj_window.get_process_id(),
            target_pixels['x'],
            target_pixels['y'],
            target_pixels['width'],
            target_pixels['height']
        )

        # no need to continue if the relevant screen is found
        break
