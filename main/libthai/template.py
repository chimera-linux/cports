pkgname = "libthai"
pkgver = "0.1.28"
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
sha256 = "ffe0a17b4b5aa11b153c15986800eca19f6c93a4025ffa5cf2cab2dcdf1ae911"

if self.cross_build:
    hostmakedepends += ["libdatrie"]

@subpackage("libthai-static")
def _static(self):
    return self.default_static()

@subpackage("libthai-devel")
def _devel(self):
    return self.default_devel()
