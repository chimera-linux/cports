pkgname = "slick-greeter"
pkgver = "2.0.7"
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
sha256 = "ad5067e9ed3e6b83026a06c804652c7700dc4b4a82e625af6cd141e145a43e9a"
hardening = ["vis"]


def post_install(self):
    # Automatically set slick-greeter as the LightDM greeter
    self.install_file(
        "debian/90-slick-greeter.conf", "usr/share/lightdm/lightdm.conf.d"
    )
