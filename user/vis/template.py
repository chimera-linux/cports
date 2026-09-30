pkgname = "vis"
pkgver = "0.9"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "lua5.5-devel",
    "lua5.5-lpeg",
    "ncurses-devel",
]
checkdepends = ["vim"]
depends = ["lua5.5-lpeg"]
pkgdesc = "Modern, legacy-free, simple yet efficient vim-like text editor"
license = "ISC"
url = "https://github.com/martanne/vis"
source = f"https://github.com/martanne/vis/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bd37ffba5535e665c1e883c25ba5f4e3307569b6d392c60f3c7d5dedd2efcfca"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vise")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vise.1",
    )
