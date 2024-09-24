pkgname = "lowdown"
pkgver = "1.1.1"
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
source = f"{url}/snapshots/lowdown.tar.gz"
sha256 = "3b1a4a9db44b0ea621189f107ff0dd6dff305c35209f46c17382b71555a3567e"
hardening = ["vis", "cfi"]


def init_configure(self):
    self.configure_args += [f"LDFLAGS={self.get_ldflags(shell=True)}"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("lowdown-devel")
def _(self):
    return self.default_devel()
