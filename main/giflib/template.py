pkgname = "giflib"
pkgver = "5.2.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["xmlto"]
pkgdesc = "Library to handle, display and manipulate GIFs"
license = "MIT"
url = "https://sourceforge.net/projects/giflib"
source = f"$(SOURCEFORGE_SITE)/giflib/giflib-{pkgver}.tar.gz"
sha256 = "be7ffbd057cadebe2aa144542fd90c6838c6a083b5e8a9048b8ee3b66b29d5fb"
tool_flags = {"CFLAGS": ["-fPIC"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("giflib-devel")
def _(self):
    return self.default_devel()


@subpackage("giflib-progs")
def _(self):
    return self.default_progs()
