pkgname = "libxo"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-dependency-tracking"]
hostmakedepends = ["pkgconf", "gettext-tiny"]
pkgdesc = "Library for generating text, XML, JSON, and HTML output"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/Juniper/libxo"
source = f"https://github.com/Juniper/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9f2f276d7a5f25ff6fbfc0f38773d854c9356e7f985501627d0c0ee336c19006"
options = ["bootstrap"]

if not current.bootstrapping:
    makedepends = ["gettext-tiny-devel"]
else:
    configure_args += ["--disable-gettext"]

def post_patch(self):
    self.mkdir("libxo/sys")
    self.cp(self.files_path / "queue.h", "libxo/sys")

@subpackage("libxo-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("libxo-progs")
def _progs(self):
    return self.default_progs(man = True)
