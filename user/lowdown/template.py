pkgname = "lowdown"
pkgver = "3.0.1"
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
sha256 = "ac9ea2b51c8bd59350c7bf8db5e2067e9d961b1f48d362cd8a56b022850e965c"


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
