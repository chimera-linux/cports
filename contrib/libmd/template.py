pkgname = "libmd"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr"
]
hostmakedepends = ["pkgconf"]
pkgdesc = "Message Digest functions from BSD systems"
maintainer = "vazub <chimera@zubko.cc>"
license = "BSD-3-Clause AND BSD-2-Clause AND ISC AND Beerware AND custom:none"
url = "https://www.hadrons.org/software/libmd"
source = f"https://archive.hadrons.org/software/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f51c921042e34beddeded4b75557656559cf5b1f2448033b4c1eec11c07e530f"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libmd-devel")
def _devel(self):
    return self.default_devel()
