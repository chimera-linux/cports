pkgname = "coeurl"
pkgver = "0.3.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=true"]
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "doctest",
    "libevent-devel",
    "spdlog-devel",
]
pkgdesc = "Asynchronous libcurl wrapper"
license = "MIT"
url = "https://nheko.im/nheko-reborn/coeurl"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "7c2497a3305c90a7c1cf2d3a840f240abc472555520e8b8f241b64703c4e7e74"
# need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("coeurl-devel")
def _(self):
    return self.default_devel()
