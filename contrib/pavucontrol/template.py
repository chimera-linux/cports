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
source = (
    f"$(FREEDESKTOP_SITE)/pulseaudio/pavucontrol/pavucontrol-{pkgver}.tar.xz"
)
sha256 = "85c860d68ff1f82cd98c72a9257184bee39299578ab122d29bc51ecbecfbf65b"
