# iTerm2_ChangeBG

Modify the background image of your iTerm2 window using keybindings

Some setup required! Visit https://iterm2.com/python-api/ for information on how to setup and run this script.

## Features

This script is a Daemon that registers functions within the iTerm2 RPC API.
This allows them to be executed using any keybindings of your choice within iTerm2.
(https://iterm2.com/python-api/tutorial/rpcs.html)

The following functions are provided:

- "rand_bg": change your iTerm2 background image to a random image in a directory
  (replace "/Users/rioedwards/Pictures/iterm_bg_photos" with your own dir path)
- "blend_more" & "blend_less": increase and decrease the amount of blend between the image and your background color
- "transparency_down" & "transparency_up": increase and decrease the transparency of your window

## Preview

![Preview](./ChangeBg_Showcase.gif)
