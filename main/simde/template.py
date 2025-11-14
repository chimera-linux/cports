pkgname = "simde"
pkgver = "0.8.4_rc2"
pkgrel = 0
build_style = "meson"
# fail to build by missing roundeven symbol
configure_args = ["-Dtests=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "SIMD wrapper implementation with non-native fallbacks"
license = "MIT"
url = "https://github.com/simd-everywhere/simde"
source = f"{url}/archive/refs/tags/v{pkgver.replace('_', '-')}.tar.gz"
sha256 = "687364c96422334e45dc3db278a022934de5e611a740fae6bdfdd05627bbdb78"


def post_install(self):
    self.install_license("COPYING")
