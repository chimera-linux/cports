pkgname = "nghttp2"
pkgver = "1.50.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-python-bindings"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "openssl-devel", "libevent-devel", "libev-devel",
    "c-ares-devel", "jansson-devel", "libxml2-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "af24007e34c18c782393a1dc3685f8fd5b50283e90a9191d25488eb50aa2c825"

def post_install(self):
    self.install_license("COPYING")

@subpackage("nghttp2-devel")
def _devel(self):
    return self.default_devel()
