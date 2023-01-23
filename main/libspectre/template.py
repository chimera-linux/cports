pkgname = "libspectre"
pkgver = "0.2.11"
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
sha256 = "79d44d65f835c5114592b60355d2fce117bace5c47a62fc63a07f10f133bd49c"
hardening = ["vis", "cfi"]

@subpackage("libspectre-devel")
def _devel(self):
    return self.default_devel()
