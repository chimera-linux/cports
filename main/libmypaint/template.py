pkgname = "libmypaint"
pkgver = "1.6.1"
pkgrel = 0
build_style = "gnu_configure"
# fails to regen
configure_gen = []
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "intltool",
    "pkgconf",
]
makedepends = ["glib-devel", "json-glib-devel", "json-c-devel", "gegl-devel"]
pkgdesc = "MyPaint brush engine library"
license = "ISC"
url = "https://github.com/mypaint/libmypaint"
source = f"{url}/releases/download/v{pkgver}/libmypaint-{pkgver}.tar.xz"
sha256 = "741754f293f6b7668f941506da07cd7725629a793108bb31633fb6c3eae5315f"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libmypaint-devel")
def _(self):
    return self.default_devel()
