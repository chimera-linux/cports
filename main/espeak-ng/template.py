pkgname = "espeak-ng"
pkgver = "1.51.1"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["pcaudiolib-devel"]
provides = [self.with_pkgver("espeak-ng-vim")]
pkgdesc = "Multilingual software speech synthesizer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/espeak-ng/espeak-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0823df5648659dcb67915baaf99118dcc8853639f47cadaa029c174bdd768d20"
# FIXME: a bunch fail for unknown reasons
options = ["!check"]


@subpackage("espeak-ng-devel")
def _(self):
    return self.default_devel()
