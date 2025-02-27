pkgname = "sassc"
pkgver = "3.6.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libsass-devel"]
pkgdesc = "Command line driver for libsass"
license = "MIT"
url = "https://github.com/sass/sassc"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "608dc9002b45a91d11ed59e352469ecc05e4f58fc1259fc9a9f5b8f0f8348a03"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
