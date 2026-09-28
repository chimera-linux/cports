pkgname = "tini"
pkgver = "0.19.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libatomic-chimera-devel",
    "libatomic-chimera-devel-static",
    "libunwind-devel",
    "libunwind-devel-static",
    "musl-devel",
    "musl-devel-static",
]
pkgdesc = "Small init for containers"
license = "MIT"
url = "https://github.com/krallin/tini"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0fd35a7030052acd9f58948d1d900fe1e432ee37103c5561554408bdac6bbf0d"


def post_install(self):
    self.install_license("LICENSE")
