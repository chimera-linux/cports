pkgname = "slick-greeter"
pkgver = "2.2.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "glib-devel", "meson", "pkgconf", "vala"]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libx11-devel",
    "libxext-devel",
    "lightdm-devel",
    "pixman-devel",
]
depends = ["lightdm", "python-gobject", "setxkbmap", "xinput"]
pkgdesc = "Slick-looking LightDM greeter"
license = "GPL-3.0-or-later"
url = "https://github.com/linuxmint/slick-greeter"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f685da6ca9d97329b4b200077d12db0ad4f9964d4515479e6c00bba721ab0626"


def post_install(self):
    # set as the default lightdm greeter
    self.install_file(
        "debian/90-slick-greeter.conf", "usr/share/lightdm/lightdm.conf.d"
    )
