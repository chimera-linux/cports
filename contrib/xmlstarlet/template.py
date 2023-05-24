pkgname = "xmlstarlet"
pkgver = "1.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libxml-prefix=/usr", "--with-libxslt-prefix=/usr"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "xsltproc"]
makedepends = ["libxslt-devel", "libxml2-devel"]
pkgdesc = "Command line utilities for XML manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xmlstar.sourceforge.net"
source = (
    f"$(SOURCEFORGE_SITE)/xmlstar/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "15d838c4f3375332fd95554619179b69e4ec91418a3a5296e7c631b7ed19e7ca"
options = ["!cross"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
