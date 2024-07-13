pkgname = "got"
pkgver = "0.101"
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
    "zlib-ng-compat-devel",
]
checkdepends = ["git"]
pkgdesc = "VCS prioritizing simplicity over flexibily"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://gameoftrees.org"
source = f"{url}/releases/portable/got-portable-{pkgver}.tar.gz"
sha256 = "25064182c731a0cbf80e48bbeecf2d628e2be41046f84aec0d89d8e7f6a6dcc0"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
