pkgname = "libthai"
pkgver = "0.1.29"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_install_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libdatrie-devel"]
pkgdesc = "Thai language support routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://linux.thai.net/projects/libthai"
source = f"https://linux.thai.net/pub/ThaiLinux/software/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fc80cc7dcb50e11302b417cebd24f2d30a8b987292e77e003267b9100d0f4bcd"

if self.profile().cross:
    hostmakedepends += ["libdatrie"]

@subpackage("libthai-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
