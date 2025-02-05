pkgname = "got"
pkgver = "0.108"
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
    "musl-devel",
    "ncurses-devel",
    "openssl3-devel",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["git"]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "6c8d320add3587ae47c06da32d41fee4087ed661931ba64dc6de77bf432bd3e2"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
