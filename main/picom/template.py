pkgname = "picom"
pkgver = "11.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["asciidoc", "meson", "pkgconf"]
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
sha256 = "1c1063936faf09ed9bba726e7737a562564b7a5f8cdef79d48fcdaf3669a4df4"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("LICENSES/MIT")
