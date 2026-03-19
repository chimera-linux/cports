pkgname = "lowdown"
pkgver = "3.1.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "PREFIX=/usr",
    "MANDIR=/usr/share/man",
]
make_cmd = "bmake"
make_install_args = ["install_libs"]
make_check_target = "regress"
hostmakedepends = ["bmake", "pkgconf"]
pkgdesc = "Markdown translator"
license = "ISC"
url = "https://kristaps.bsd.lv/lowdown"
source = f"{url}/snapshots/lowdown-{pkgver}.tar.gz"
sha256 = "59b2cf35bf32fe602c92f33ae917a71e0b2ea76a67bbe48fbae901a8efc6fef3"


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
