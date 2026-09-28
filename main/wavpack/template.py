pkgname = "wavpack"
pkgver = "5.8.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
pkgdesc = "Hybrid lossless audio compression"
license = "BSD-3-Clause"
url = "https://www.wavpack.com"
source = f"https://github.com/dbry/WavPack/releases/download/{pkgver}/wavpack-{pkgver}.tar.xz"
sha256 = "7322775498602c8850afcfc1ae38f99df4cbcd51386e873d6b0f8047e55c0c26"


def post_install(self):
    self.install_license("COPYING")


@subpackage("wavpack-devel")
def _(self):
    return self.default_devel()


@subpackage("wavpack-progs")
def _(self):
    return self.default_progs()
