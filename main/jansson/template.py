pkgname = "jansson"
pkgver = "2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for encoding, decoding and manipulating JSON data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.digip.org/jansson"
source = f"https://github.com/akheron/jansson/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5798d010e41cf8d76b66236cfb2f2543c8d082181d16bc3085ab49538d4b9929"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("jansson-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
