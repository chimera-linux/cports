pkgname = "pavucontrol"
pkgver = "5.0"
pkgrel = 3
_commit = "c330506815f78f77f6685cb40749679eae789d63"
build_style = "meson"
hostmakedepends = ["gettext", "meson", "lynx", "pkgconf"]
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
source = f"https://gitlab.freedesktop.org/pulseaudio/pavucontrol/-/archive/{_commit}.tar.gz"
sha256 = "51c4b4002836aa53ddef88b16300b4ab5ef983b4e3a36b38274843e8d6447e9d"


def post_extract(self):
    self.mv(
        "src/pavucontrol.desktop.in",
        "src/org.pulseaudio.pavucontrol.desktop.in",
    )
