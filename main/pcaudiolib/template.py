pkgname = "pcaudiolib"
pkgver = "1.3"
pkgrel = 0
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
sha256 = "86edb75048eec7fcd8d74f9568f051d50b4781982215095b96ba9c2c9c7c159b"


@subpackage("pcaudiolib-devel")
def _(self):
    return self.default_devel()
