pkgname = "lowdown"
pkgver = "1.1.0"
pkgrel = 1
build_style = "configure"
configure_args = [
    "PREFIX=/usr",
    "MANDIR=/usr/share/man",
]
make_install_args = ["install_libs"]
make_check_target = "regress"
hostmakedepends = ["pkgconf"]
pkgdesc = "Markdown translator"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://kristaps.bsd.lv/lowdown"
source = f"{url}/snapshots/lowdown.tar.gz"
sha256 = "f31e3950c4732b1e409174fa092eca40c55be77a448ee2818df987979d7b0879"
hardening = ["vis", "cfi"]


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
