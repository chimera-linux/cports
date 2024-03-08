pkgname = "got"
pkgver = "0.96"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "bison",
    "gmake",
    "pkgconf",
]
makedepends = [
    "libmd-devel",
    "libbsd-devel",
    "libevent-devel",
    "linux-headers",
    "musl-devel",
    "ncurses-devel",
    "libuuid-devel",
    "zlib-devel",
]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "fd1eebe8826d824b8d430a0bc72b3fd477175be9773d59239cf5e9845a40153b"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
