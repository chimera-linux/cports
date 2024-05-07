pkgname = "got"
pkgver = "0.99"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=/usr",
    "--with-gitwrapper-git-libexec=/usr/libexec/git-core",
]
make_cmd = "gmake"
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "bison",
    "gmake",
    "pkgconf",
]
makedepends = [
    "libbsd-devel",
    "libevent-devel",
    "libretls-devel",
    "libuuid-devel",
    "linux-headers",
    "musl-devel",
    "ncurses-devel",
    "zlib-devel",
]
checkdepends = ["git"]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "aea408353a02b2e3ad9b4d1b7607900269af97986d40998c57f10acdf0fa1e38"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
