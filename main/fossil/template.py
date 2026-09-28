pkgname = "fossil"
pkgver = "2.26"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--json",
    "--with-th1-docs",
    "--with-th1-hooks",
    "--with-tcl=1",
    "--with-tcl-private-stubs",
]
configure_gen = []
make_check_target = "test"
makedepends = ["openssl3-devel", "zlib-ng-compat-devel", "tcl-devel"]
checkdepends = ["tcl"]
pkgdesc = "Distributed software configuration management system"
license = "BSD-2-Clause"
url = "https://fossil-scm.org"
source = f"https://fossil-scm.org/home/tarball/version-{pkgver}/fossil-src-{pkgver}.tar.gz"
sha256 = "a9be104c8055ada40985a158392d73f3c84829accb5b5d404e361fea360774c2"
# tests are unmaintained: https://fossil-scm.org/forum/forumpost/77cd773882607d94
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYRIGHT-BSD2.txt")
    self.install_man("fossil.1")
