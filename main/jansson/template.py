pkgname = "jansson"
pkgver = "2.14.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Library for encoding, decoding and manipulating JSON data"
license = "MIT"
url = "https://www.digip.org/jansson"
source = f"https://github.com/akheron/jansson/releases/download/v{pkgver}/jansson-{pkgver}.tar.gz"
sha256 = "2521cd51a9641d7a4e457f7215a4cd5bb176f690bc11715ddeec483e85d9e2b3"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("jansson-devel")
def _(self):
    return self.default_devel()
