pkgname = "picom"
pkgver = "12.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunittest=true", "-Dwith_docs=true"]
hostmakedepends = ["asciidoctor", "meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libconfig-devel",
    "libepoxy-devel",
    "libev-devel",
    "libx11-devel",
    "libxcb-devel",
    "mesa-devel",
    "pcre2-devel",
    "pixman-devel",
    "uthash",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-renderutil-devel",
]
pkgdesc = "Standalone compositor for X11"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 AND MIT"
url = "https://github.com/yshui/picom"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "627fa5d7c590df3ba8d2c41eb35d3859f7826bd28fa49e92a0e04fb60ed77904"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("LICENSES/MIT")


@subpackage("picom-devel")
def _(self):
    return self.default_devel()
