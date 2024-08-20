pkgname = "muparser"
pkgver = "2.3.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libomp-devel",
]
pkgdesc = "Qt implementation of freedesktop.org xdg specs"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "BSD-2-Clause"
url = "https://beltoforion.de/en/muparser"
source = f"https://github.com/beltoforion/muparser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0c3fa54a3ebf36dda0ed3e7cd5451c964afbb15102bdbcba08aafb359a290121"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("muparser-devel")
def _(self):
    return self.default_devel()
