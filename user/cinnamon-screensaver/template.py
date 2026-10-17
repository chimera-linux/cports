pkgname = "cinnamon-screensaver"
pkgver = "6.6.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared", "-Dpam-prefix=/usr/lib"]
hostmakedepends = ["glib-devel", "gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "linux-pam-devel",
    "xdotool-devel",
]
depends = [
    "cinnamon-desktop",
    "libgnomekbd",
    "python-cairo",
    "python-gobject",
    "python-setproctitle",
    "python-xapp",
    "python-xlib",
    "xapp",
]
pkgdesc = "Screen locker and screensaver for the Cinnamon desktop"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-screensaver/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d873cc22eb50db8b9339b546b9133945eee3a1458682136cb475a49252568fad"
options = ["!cross"]
