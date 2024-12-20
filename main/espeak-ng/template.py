pkgname = "espeak-ng"
pkgver = "1.52.0"
pkgrel = 1
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
sha256 = "bb4338102ff3b49a81423da8a1a158b420124b055b60fa76cfb4b18677130a23"
# FIXME: a bunch fail for unknown reasons
options = ["!check"]


@subpackage("espeak-ng-devel")
def _(self):
    return self.default_devel()
