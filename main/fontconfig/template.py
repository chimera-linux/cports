pkgname = "fontconfig"
pkgver = "2.13.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static", "--enable-docs",
    f"--with-cache-dir=/var/cache/{pkgname}",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gperf", "gmake"]
makedepends = ["libexpat-devel", "freetype-bootstrap", "libuuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/release/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f655dd2a986d7aa97e052261b36aa67b0a64989496361eca8d604e6414006741"

def post_install(self):
    self.install_license("COPYING")

@subpackage("fontconfig-static")
def _static(self):
    return self.default_static()

@subpackage("fontconfig-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("fontconfig-doc")
def _doc(self):
    return self.default_doc()
