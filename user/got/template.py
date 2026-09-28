pkgname = "got"
pkgver = "0.124"
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
sha256 = "8ff38e980a9343aec4152bb5ac1fc916ca093cf655c73a786fb8bd87a50d9c44"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
