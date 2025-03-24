pkgname = "got"
pkgver = "0.110"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=/usr",
    "--libexecdir=/usr/lib/got",
    "--with-gitwrapper-git-libexec=/usr/lib/git-core",
]
make_check_target = "tests"
hostmakedepends = [
    "automake",
    "bison",
    "pkgconf",
]
makedepends = [
    "libbsd-devel",
    "libevent-devel",
    "libretls-devel",
    "linux-headers",
    "ncurses-devel",
    "openssl3-devel",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["git"]
pkgdesc = "VCS prioritizing simplicity over flexibily"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "3635e41205e7f85236a6e76ff785d3d8997131cf353c8cdf6f6d25c031661d29"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
