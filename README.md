# Palka
Window positioning in Ubuntu

Palka will allow users to manage the placement of a window.
Idealy used with hotkeys to set the active window.
Created as a personal first Python project.

**Work in Progress**

It should mainly function the same as *windowpad* which only works in MS Windows.  
This should be a Ubuntu eqivalent.

## Install

For now just clone this repository and make sure `wmctrl` is installed.
Made using Python 3.4 other versions not tested. Pretty sure won't work below 3
Better installer is on the wish list

## Parameters

**help:** will show all other default values.
**install:** Pretty much unimplemented at the moment

Dimensions of the window:

 - **xoffset:** Percentage where the left border of the window should be on the screen. Value _0_(left) to _100_(right) defaults to _0_
 - **yoffset:** Percentage where the top border of the window should be on the screen. Value _0_(top) to _100_(bottom) defaults to _0_
 - **width:** Width of the window in percentages. Use negative percentages to flip it arround. Value _-100_ to _100_ defaults to _50_
 - **height:** Height of the window in percentages. Use negative percentages to flip it arround. Value _-100_ to _100_ defaults to _50_

## Example usages

Place the window at the left half width full height:

    python3 palka.py --xoffset 0 --yoffset 0 --height 100 --width 50

Quarter top left:

    python3 palka.py --xoffset 0 --yoffset 0 --height 50 --width 50

Quarter top right:

    python3 palka.py --xoffset 100 --yoffset 0 --height 50 --width -50

Or without the negative:

    python3 palka.py --xoffset 50 --yoffset 0 --height 50 --width 50


Quarter bottom left:

    python3 palka.py --xoffset 0 --yoffset 100 --height -50 --width 50

Quarter bottom right:

    python3 palka.py --xoffset 100 --yoffset 100 --height -50 --width -50

## Roadmap

**Need to fix before real use is doable**

  1) Switch to other display
  2) Override Maximize
  3) Real maximize (100 widht & height) won't activate maximize
  4) window ID as argument
  5) Automaticly setup hotkeys

**After that**

   1) Real installer
   2) Unity bug



