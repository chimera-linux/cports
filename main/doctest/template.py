pkgname = "doctest"
pkgver = "2.4.11"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DDOCTEST_USE_STD_HEADERS=ON",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Single-header testing framework"
license = "MIT"
url = "https://github.com/doctest/doctest"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "632ed2c05a7f53fa961381497bf8069093f0d6628c5f26286161fbd32a560186"


def post_install(self):
    self.install_license("LICENSE.txt")
