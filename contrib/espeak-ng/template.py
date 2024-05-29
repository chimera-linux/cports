pkgname = "espeak-ng"
pkgver = "1.51.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = ["pcaudiolib-devel"]
pkgdesc = "Multilingual software speech synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/espeak-ng/espeak-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0823df5648659dcb67915baaf99118dcc8853639f47cadaa029c174bdd768d20"
# FIXME: a bunch fail for unknown reasons
options = ["!check"]


@subpackage("espeak-ng-devel")
def _devel(self):
    return self.default_devel()


@subpackage("espeak-ng-vim")
def _vim(self):
    self.pkgdesc = f"{pkgdesc} (vim syntax)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "vim"]
    return ["usr/share/vim"]
