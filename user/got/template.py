pkgname = "got"
pkgver = "0.98.2"
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
    "libretls-devel",
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
sha256 = "ff5d4ad9922edf1c8055b2398650972fd463c809590dbe78e2eab1bf78a150c8"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
