pkgname = "vis"
pkgver = "0.9_git20260630"
_gitrev = "0515140cfc4097e388302c8167cbe2660b4441cf"
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
sha256 = "525e2e5eca837f32bd0627fb62c7c390b5d3c4c7348aee2e49189d6d62f8936b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vis-editor")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vis-editor.1",
    )
