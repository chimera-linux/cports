pkgname = "slick-greeter"
pkgver = "2.0.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "meson", "pkgconf", "vala"]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libx11-devel",
    "lightdm-devel",
    "pixman-devel",
    "xapp-devel",
]
depends = ["gtk+3", "lightdm", "python-gobject"]
pkgdesc = "Slick-looking LightDM greeter"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxmint/slick-greeter"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "446fcda5776839013eb91fbf0c95fcd2aa70c331e570edda8aacd0d60b219de1"
hardening = ["vis"]


def post_install(self):
    # Automatically set slick-greeter as the LightDM greeter
    self.install_file(
        "debian/90-slick-greeter.conf", "usr/share/lightdm/lightdm.conf.d"
    )
