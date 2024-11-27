pkgname = "simde"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
# fail to build by missing roundeven symbol
configure_args = ["-Dtests=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "SIMD wrapper implementation with non-native fallbacks"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/simd-everywhere/simde"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ed2a3268658f2f2a9b5367628a85ccd4cf9516460ed8604eed369653d49b25fb"


def post_install(self):
    self.install_license("COPYING")
