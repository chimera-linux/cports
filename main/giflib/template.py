pkgname = "giflib"
pkgver = "5.2.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "xmlto"]
pkgdesc = "Library to handle, display and manipulate GIFs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://sourceforge.net/projects/giflib"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "31da5562f44c5f15d63340a09a4fd62b48c45620cd302f77a6d9acf0077879bd"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("giflib-static")
def _static(self):
    return self.default_static()

@subpackage("giflib-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("giflib-progs")
def _progs(self):
    return self.default_progs(man = True)
