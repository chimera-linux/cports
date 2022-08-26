pkgname = "nghttp2"
pkgver = "1.49.0"
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
sha256 = "b0cfd492bbf0b131c472e8f6501c9f4ee82b51b68130f47b278c0b7c9848a66e"

def post_install(self):
    self.install_license("COPYING")

@subpackage("nghttp2-devel")
def _devel(self):
    return self.default_devel()
