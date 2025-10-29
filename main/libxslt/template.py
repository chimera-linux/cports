pkgname = "libxslt"
pkgver = "1.1.43"
pkgrel = 0
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
license = "MIT"
url = "http://xmlsoft.org/XSLT"
source = f"$(GNOME_SITE)/libxslt/{pkgver[: pkgver.rfind('.')]}/libxslt-{pkgver}.tar.xz"
sha256 = "5a3d6b383ca5afc235b171118e90f5ff6aa27e9fea3303065231a6d403f0183a"


def post_extract(self):
    self.rm("tests/general/bug-219.*", glob=True)


def post_install(self):
    self.install_license("Copyright")


@subpackage("libxslt-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/xsltConf.sh"])


@subpackage("libxslt-progs")
def _(self):
    self.renames = ["xsltproc"]

    return self.default_progs()
