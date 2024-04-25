pkgname = "fossil"
pkgver = "2.24"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-internal-sqlite",
    "--json",
    "--with-th1-docs",
    "--with-th1-hooks",
    "--with-tcl=1",
    "--with-tcl-private-stubs",
]
configure_gen = []
make_check_target = "test"
makedepends = ["openssl-devel", "zlib-devel", "sqlite-devel", "tcl-devel"]
checkdepends = ["tcl", "tcllib"]
pkgdesc = "Distributed software configuration management system"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause"
url = "https://fossil-scm.org"
source = f"https://fossil-scm.org/home/tarball/version-{pkgver}/fossil-src-{pkgver}.tar.gz"
sha256 = "e6f5a559369bf16baf539e69e6d0cea5a6410efa9a6e7f160c7a4932080413be"
# tests are unmaintained: https://fossil-scm.org/forum/forumpost/77cd773882607d94
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYRIGHT-BSD2.txt")
    self.install_man("fossil.1")
