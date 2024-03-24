pkgname = "got"
pkgver = "0.97"
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
sha256 = "e07a4894a458503a32982047f064bc0c35da6349d8895be8b69064c2094e3b72"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
