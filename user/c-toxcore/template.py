pkgname = "c-toxcore"
pkgver = "0.2.22"
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
license = "GPL-3.0-only"
url = "https://github.com/TokTok/c-toxcore"
source = f"{url}/releases/download/v{pkgver}/c-toxcore-v{pkgver}.tar.gz"
sha256 = "276d447eb94e9d76e802cecc5ca7660c6c15128a83dfbe4353b678972aeb950a"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("c-toxcore-devel")
def _(self):
    return self.default_devel()
