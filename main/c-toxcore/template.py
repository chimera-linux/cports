pkgname = "c-toxcore"
pkgver = "0.2.19"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DUNITTEST=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtest-devel",
    "libconfig-devel",
    "libsodium-devel",
    "libvpx-devel",
    "linux-headers",
    "opus-devel",
]
pkgdesc = "Tox communication project"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/TokTok/c-toxcore"
source = f"{url}/releases/download/v{pkgver}/c-toxcore-{pkgver}.tar.gz"
sha256 = "8b418f6470db085cf59a9915685613556556df2bf427148f1814b7b118628594"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("c-toxcore-devel")
def _(self):
    return self.default_devel()
