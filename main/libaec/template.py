pkgname = "libaec"
pkgver = "1.1.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Adaptive entropy coding library"
license = "BSD-2-Clause"
url = "https://gitlab.dkrz.de/k202009/libaec"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "95439e861968cb0638a10b0bbdb37c9a10df1b22c5ee0293902acdbc68140f53"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("libaec-devel")
def _(self):
    return self.default_devel()
