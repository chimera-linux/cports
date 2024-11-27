pkgname = "pcaudiolib"
pkgver = "1.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-alsa",
    "--without-oss",
]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["alsa-lib-devel"]
pkgdesc = "Portable C audio library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/espeak-ng/pcaudiolib"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "44b9d509b9eac40a0c61585f756d76a7b555f732e8b8ae4a501c8819c59c6619"


@subpackage("pcaudiolib-devel")
def _(self):
    return self.default_devel()
