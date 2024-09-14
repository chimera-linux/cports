pkgname = "xserver-xorg"
pkgver = "1.0"
pkgrel = 2
build_style = "meta"
depends = [
    "xserver-xorg-minimal",
    "fonts-xorg",
    # additional utilities and other packages for most users
    "iceauth",
    "setxkbmap",
    "transset",
    "xbacklight",
    "xcmsdb",
    "xcursorgen",
    "xdpyinfo",
    "xev",
    "xeyes",
    "xgamma",
    "xhost",
    "xinput",
    "xkbcomp",
    "xkill",
    "xlsatoms",
    "xlsclients",
    "xlsfonts",
    "xmodmap",
    "xpr",
    "xprop",
    "xrandr",
    "xrdb",
    "xrefresh",
    "xset",
    "xsetroot",
    "xvinfo",
    "xwd",
    "xwininfo",
    "xwud",
]
pkgdesc = "Default X.org metapackage"
subdesc = "with common apps"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://xorg.freedesktop.org"
