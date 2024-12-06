pkgname = "lowdown"
pkgver = "1.3.1"
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
sha256 = "56593b6a0ff3400498bc589472c444bb2bf05b518312576bf7a4b0069bb34220"
hardening = ["vis", "cfi"]


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
