pkgname = "lowdown"
pkgver = "1.3.0"
pkgrel = 0
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
source = f"{url}/snapshots/lowdown-{pkgver}.tar.gz"
sha256 = "e9e157b1a0326f2352880e2f420f1159d227a1c57015ae11ff6f582c5de58418"
hardening = ["vis", "cfi"]


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
