pkgname = "jansson"
pkgver = "2.13.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
checkdepends = ["iana-etc"]
pkgdesc = "Library for encoding, decoding and manipulating JSON data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.digip.org/jansson"
source = f"https://github.com/akheron/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "f22901582138e3203959c9257cf83eba9929ac41d7be4a42557213a22ebcc7a0"

def pre_configure(self):
    self.do("autoreconf", ["-if"])

def post_install(self):
    self.install_license("LICENSE")

@subpackage("jansson-devel")
def _devel(self):
    return self.default_devel()
