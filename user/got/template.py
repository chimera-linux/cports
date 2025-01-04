pkgname = "got"
pkgver = "0.106"
pkgrel = 1
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
    "libuuid-devel",
    "linux-headers",
    "musl-devel",
    "ncurses-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["git"]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "3079d742c125047de339dd923d75d0b960995a3a4b567ed08ef36d112bdb07cc"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
