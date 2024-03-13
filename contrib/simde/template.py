pkgname = "simde"
pkgver = "0.7.6"
pkgrel = 0
build_style = "meson"
# fail to build by missing roundeven symbol
configure_args = ["-Dtests=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "SIMD wrapper implementation with non-native fallbacks"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/simd-everywhere/simde"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c63e6c61392e324728da1c7e5de308cb31410908993a769594f5e21ff8de962b"


def post_install(self):
    self.install_license("COPYING")
