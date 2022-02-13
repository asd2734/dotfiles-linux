# Original work Copyright (c) 2010 Aldo Cortesi
# Original work Copyright (c) 2010, 2014 dequis
# Original work Copyright (c) 2012 Randall Ma
# Original work Copyright (c) 2012-2014 Tycho Andersen
# Original work Copyright (c) 2012 Craig Barnes
# Original work Copyright (c) 2013 horsik
# Original work Copyright (c) 2013 Tao Sauvage
# Modified work Copyright (c) 2021 Alex Choi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from enum import Enum

# Application variables
mod = "mod4"
terminal = "kitty"

# Color scheme
#   color names as defined in htmlcsscolor.com
class Color( Enum ):
    MIDNIGHT_EXPRESS =      "#282A36" # dark navy
    SLATE_BLUE =            "#6A5ACD" # purplish
    MAYA_BLUE =             "#57C7FF" # blue
    DODGER_BLUE =           "#1E90FF" # neon blue
    ELECTRIC_BLUE =         "#8BE9FD" # light blue
    BLIZZARD_BLUE =         "#A8E3F1" # pastel blue
    FIREBRICK =             "#B22222" # brick red
    SUNSET_ORANGE =         "#FF5555" # salmonish orange
    MACARONI_AND_CHEESE =   "#FFB86C" # light orange
    SCREAMIN_GREEN =        "#5AF78E" # bright light green
    TIDAL =                 "#F1FA8C" # neon yellow
    NEON_PINK =             "#FF6AC1" # neon pink
    DUST_STORM =            "#E8C5BE" # beige
    ALABASTER =             "#F1F1F0" # really really light grey (almost white)
    MEDIUM_PURPLE =         "#835FD3" # just purple
    MEDIUM_ORCHID =         "#BA55D3" # darker orchid
    ORCHID =                "#DA70D6" # pinkish
    PERFUME =               "#BD9CF9" # lavender

# Key bindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Menu 
    Key( [mod], "space", lazy.spawn( "rofi -show run" ), desc="Run rofi in run mode" ),

    # Volume
    Key( [], "XF86AudioRaiseVolume", lazy.spawn( "amixer -c 0 -q set Master 1dB+" ) ),
    Key( [], "XF86AudioLowerVolume", lazy.spawn( "amixer -c 0 -q set Master 1dB-" ) ),
    Key( [], "XF86AudioMute", lazy.spawn( "amixer -c 0 -q set Master toggle" ) ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
'''
layout_border = {
    'border_focus': bar_colors['electric_blue'],
    'border_width': 2,
    'margin': 3,
    'single_border_width': 0,
    'single_margin': 3 }
'''
layouts = [
    layout.Columns( border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack Nerd Font Bold',
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    font='mononoki Nerd Font Bold',
                    fmt='{:3.3}',
                    padding=5,
                    foreground=Color.ALABASTER.value,
                    background=Color.SUNSET_ORANGE.value ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper() ),
                widget.Systray(),
                widget.TextBox( 
                    font="mononoki Nerd Font Bold",
                    fmt="cpu" ),
                widget.CPUGraph( 
                    frequency=.5,
                    width=60,
                    margin_y=4,
                    border_color=Color.DODGER_BLUE.value,
                    graph_color=Color.DODGER_BLUE.value,
                    fill_color=Color.DODGER_BLUE.value ),
                widget.TextBox( 
                    font="mononoki Nerd Font Bold",
                    fmt="mem" ),
                widget.MemoryGraph( 
                    frequency=.5,
                    width=60,
                    margin_y=4,
                    border_color=Color.MACARONI_AND_CHEESE.value,
                    graph_color=Color.MACARONI_AND_CHEESE.value,
                    fill_color=Color.MACARONI_AND_CHEESE.value ),
                widget.Net(
                    font="mononoki Nerd Font Bold",
                    fontsize=12,
                    format='d:{down: ^8.8}u:{up: ^8.8}' ),
                widget.Wlan(
                    interface="wlp3s0",
                    font="mononoki Nerd Font Bold",
                    format="wifi:{essid}",
                    padding=10,
                    background=Color.MAYA_BLUE.value, ),
                widget.Volume(
                    update_interval=.05,
                    font='mononoki Nerd Font Bold',
                    fmt="vol:{: ^3}",
                    padding=10,
                    foreground=Color.SLATE_BLUE.value,
                    background=Color.ELECTRIC_BLUE.value, ),
                widget.Battery(
                    battery=0,
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    font='mononoki Nerd Font Bold',
                    format="bat0:{percent:04.0%}",
                    padding=10,
                    show_short_text=False,
                    foreground=Color.SLATE_BLUE.value,
                    background=Color.BLIZZARD_BLUE.value, ),
                widget.Battery(
                    battery=1,
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    font='mononoki Nerd Font Bold',
                    format="bat1:{percent:04.0%}",
                    padding=10,
                    show_short_text=False,
                    foreground=Color.SLATE_BLUE.value,
                    background=Color.BLIZZARD_BLUE.value, ),
                widget.Clock(
                    font='mononoki Nerd Font Bold',
                    format='%a %m/%d %I:%M %p',
                    foreground=Color.PERFUME.value,
                    background=Color.ALABASTER.value,
                    padding=10 ),
            ],
            30,
            background=Color.MIDNIGHT_EXPRESS.value,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
