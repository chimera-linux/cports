pkgname = "libnumbertext"
pkgver = "1.0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
checkdepends = ["bash"]
pkgdesc = "Language-neutral NUMBERTEXT and MONEYTEXT implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/Numbertext/libnumbertext"
source = f"http://dev-www.libreoffice.org/src/{pkgname}-{pkgver}.tar.xz"
sha256 = "5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0"


@subpackage("libnumbertext-devel")
def _devel(self):
    return self.default_devel()
