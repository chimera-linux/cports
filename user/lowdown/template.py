pkgname = "lowdown"
pkgver = "2.0.2"
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
sha256 = "d59f2ad82f981a63051bb61d8d04c02c8c49428ac29c435dff03a92e210b0004"


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
