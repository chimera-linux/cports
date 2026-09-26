pkgname = "libkiwix"
pkgver = "14.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddoc=false",
    "-Dwerror=false",
]
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "icu-devel",
    "libmicrohttpd-devel",
    "libzim-devel",
    "mustache",
    "pugixml-devel",
    "xapian-core-devel",
    "zlib-ng-compat-devel",
]
depends = ["aria2"]
checkdepends = ["gtest-devel"]
pkgdesc = "Library providing the Kiwix software core"
license = "GPL-3.0-or-later"
url = "https://github.com/kiwix/libkiwix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cff1eb06d62ab42e1720a49f473b7d9364f02ee77a8a455c9adb26db419e0fff"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libkiwix-devel")
def _(self):
    return self.default_devel()
