pkgname = "pavucontrol"
pkgver = "6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "lynx",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "gtkmm-devel",
    "json-glib-devel",
    "libcanberra-devel",
    "libpulse-devel",
    "libsigc++-devel",
]
pkgdesc = "PulseAudio volume control"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/software/pulseaudio/pavucontrol"
source = f"https://gitlab.freedesktop.org/pulseaudio/pavucontrol/-/archive/v{pkgver}.tar.gz"
sha256 = "7d0e97790bfbfb7489bc19aacac94b395e8aaf591e21be9ee2102a7adafa2d82"
