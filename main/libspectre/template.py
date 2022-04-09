pkgname = "libspectre"
pkgver = "0.2.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
make_dir = "." # ftbfs
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["libgs-devel"]
checkdepends = ["cairo-devel"]
pkgdesc = "Small library for rendering PostScript documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/libspectre"
source = f"http://libspectre.freedesktop.org/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "cf60b2a80f6bfc9a6b110e18f08309040ceaa755210bf94c465a969da7524d07"

@subpackage("libspectre-devel")
def _devel(self):
    return self.default_devel()
