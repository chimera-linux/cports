pkgname = "libkiwix"
pkgver = "14.2.0"
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
    "python",
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
pkgdesc = "Library providing the Kiwix software core"
license = "GPL-3.0-or-later"
url = "https://github.com/kiwix/libkiwix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "244b69120d132de3079774ee439f9adfb7b556e88b9ef6ce5300f37dfc3737bc"
# no useful check target without gtest, and tests are not needed for packaging
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libkiwix-devel")
def _(self):
    return self.default_devel()
