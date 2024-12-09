pkgname = "c-toxcore"
pkgver = "0.2.20"
pkgrel = 0
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
sha256 = "a9c89a8daea745d53e5d78e7aacb99c7b4792c4400a5a69c71238f45d6164f4c"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("c-toxcore-devel")
def _(self):
    return self.default_devel()
