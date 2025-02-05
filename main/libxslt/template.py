pkgname = "libxslt"
pkgver = "1.1.42"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-python=no"]
hostmakedepends = [
    "automake",
    "docbook-xml",
    "docbook-xsl-nons",
    "libtool",
    "pkgconf",
]
makedepends = ["libgcrypt-devel", "libxml2-devel"]
pkgdesc = "GNOME XSLT parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xmlsoft.org/XSLT"
source = f"$(GNOME_SITE)/libxslt/{pkgver[: pkgver.rfind('.')]}/libxslt-{pkgver}.tar.xz"
sha256 = "85ca62cac0d41fc77d3f6033da9df6fd73d20ea2fc18b0a3609ffb4110e1baeb"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxslt-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/xsltConf.sh"])


@subpackage("libxslt-progs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("xsltproc")]

    return self.default_progs()
