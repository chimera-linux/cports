pkgname = "vis"
pkgver = "0.9_git20260726"
_gitrev = "aa99d1775c1faf2446bc294bc4072ccb661d7cd6"
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
source = f"https://github.com/martanne/vis/archive/{_gitrev}.tar.gz"
sha256 = "d70bd1058e97b4f1ff61fcace50376d44dadc9c04a1b0f5d622384e6e38e6d88"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vis-editor")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vis-editor.1",
    )
