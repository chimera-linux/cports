pkgname = "vis"
pkgver = "0.9_git20260606"
_gitrev = "462d57d190ff9f89d83e52b9496de09cd89ed045"
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
sha256 = "60b1e754ebfcb429cda75dfa4db77327e698f7cfde2eeb0489ffe0ca693da0fd"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vis-editor")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vis-editor.1",
    )
