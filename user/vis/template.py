pkgname = "vis"
pkgver = "0.9_git20250102"
_commit = "e9fb2f04e3a479c965b5d43cdf5608cccb8e498f"
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
license = "ISC"
url = "https://github.com/martanne/vis"
source = [
    f"{url}/archive/{_commit}.tar.gz",
]
sha256 = [
    "5f42e89978fee95e570cdc4f458b27c468e1ef3cb4a1d441d00d07fcb7c9a3a9",
]


def post_install(self):
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vise")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vise.1",
    )
    self.install_license("LICENSE")
