pkgname = "got"
pkgver = "0.105"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=/usr",
    "--with-gitwrapper-git-libexec=/usr/libexec/git-core",
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
sha256 = "3173e360dcd06fa241bec31fc4df862843ffedf2b010605680680b0dfd5ca244"
env = {"GOT_RELEASE": "Yes"}
hardening = ["vis", "cfi"]
# tests require pre-installing got/tog in pre_check and running ssh locally
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
