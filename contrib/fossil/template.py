pkgname = "fossil"
pkgver = "2.23"
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
sha256 = "a94aec2609331cd6890c6725b55aea43041011863f3d84fdc380415af75233e4"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYRIGHT-BSD2.txt")
    self.install_man("fossil.1")
