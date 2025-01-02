pkgname = "vis"
pkgver = "0.9"
_testver = "783b7ef67aa360f0b9bd44fa5ea47e644bc49d69"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "libtermkey-devel",
    "lua5.4-devel",
    "lua5.4-lpeg",
    "ncurses-devel",
]
depends = ["lua5.4-lpeg"]
checkdepends = ["vim"]
pkgdesc = "Modern, legacy free, simple yet efficient vim-like editor"
maintainer = "sewn <sewn@disroot.org>"
license = "ISC"
url = "https://github.com/martanne/vis"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"https://github.com/martanne/vis-test/archive/{_testver}.tar.gz",
]
source_paths = [".", "test"]
sha256 = [
    "bd37ffba5535e665c1e883c25ba5f4e3307569b6d392c60f3c7d5dedd2efcfca",
    "00302137550c07f82841723fcc9553834d2ed88f0943ffa6e22675b0d0248122",
]


def post_install(self):
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vise")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vise.1",
    )
    self.install_license("LICENSE")
