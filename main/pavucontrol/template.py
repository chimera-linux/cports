pkgname = "pavucontrol"
pkgver = "6.1"
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
sha256 = "d6e529a0e44c25a24e461036ed366a59db6e87cd74eaa0e3c6422b40102ce171"
