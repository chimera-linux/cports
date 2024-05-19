pkgname = "libass"
pkgver = "0.17.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "nasm",
]
makedepends = [
    "fontconfig-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "libunibreak-devel",
]
pkgdesc = "Portable library for SSA/ASS subtitle rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/libass/libass"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a9afb52bf76a2569263fe2038896774c991b35c0968342a03be708e56ea60c3b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libass-devel")
def _devel(self):
    return self.default_devel()
