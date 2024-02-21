pkgname = "giflib"
pkgver = "5.2.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "xmlto"]
pkgdesc = "Library to handle, display and manipulate GIFs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://sourceforge.net/projects/giflib"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "be7ffbd057cadebe2aa144542fd90c6838c6a083b5e8a9048b8ee3b66b29d5fb"
tool_flags = {"CFLAGS": ["-fPIC"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("giflib-devel")
def _devel(self):
    return self.default_devel()


@subpackage("giflib-progs")
def _progs(self):
    return self.default_progs()
