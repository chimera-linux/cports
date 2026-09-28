pkgname = "lowdown"
pkgver = "3.2.1"
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
sha256 = "664afc7c00aadbaf16cdcf7dc464e64b529f432eba9dffc950acb0d55d1be90d"


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
