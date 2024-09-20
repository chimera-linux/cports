pkgname = "libeconf"
pkgver = "0.7.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf", "doxygen"]
pkgdesc = "Config file parser"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "MIT"
url = "https://github.com/openSUSE/libeconf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4174ca94e958cbb6c8bb4ea9e6909877d6178e00b6a65349eade64a462534da0"
options = ["linkundefver"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libeconf-devel")
def _(self):
    return self.default_devel()


@subpackage("libeconf-progs")
def _(self):
    return self.default_progs()
