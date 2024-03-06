pkgname = "got"
pkgver = "0.96"
pkgrel = 0
build_style = "gnu_configure"
# broken autogen.sh
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
    "libbsd-devel",
    "libmd-devel",
    "libevent-devel",
    "ncurses-devel",
    "libuuid-devel",
    "zlib-devel",
]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = (
    f"https://gameoftrees.org/releases/portable/got-portable-{pkgver}.tar.gz"
)
sha256 = "fd1eebe8826d824b8d430a0bc72b3fd477175be9773d59239cf5e9845a40153b"
# some test fail
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
