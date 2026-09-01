pkgname = "glaze"
pkgver = "7.9.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dglaze_DEVELOPER_MODE=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "Fast serialization and reflection library for C++"
license = "MIT"
url = "https://github.com/stephenberry/glaze"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d6dee391276f5375672c35d06058e4fd8f1f30f62bae163a004b3bd13a4e2ae3"

# header-only library
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
