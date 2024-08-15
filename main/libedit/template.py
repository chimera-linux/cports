pkgname = "libedit"
pkgver = "20240711"
pkgrel = 1
_gitrev = "b1ed32d99f36fa751595473e151b7388786c0d6b"
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "4bb266fbe756593e9c6ae699c89a8c02e6e40636bb87a0f83f16525211905826"
options = ["bootstrap"]


def post_install(self):
    self.install_license("COPYING")
    # conflicts with readline-devel-man
    self.uninstall("usr/share/man/man3/history.3")
    # readline compat
    self.install_file(self.files_path / "readline.h", "usr/include/readline")
    self.install_file(self.files_path / "history.h", "usr/include/readline")
    self.install_file(self.files_path / "libhistory.so", "usr/lib")
    self.install_file(self.files_path / "libreadline.so", "usr/lib")
    self.install_link("usr/lib/libreadline.a", "libedit.a")
    self.install_link("usr/lib/libhistory.a", "libedit.a")
    self.install_link("usr/lib/pkgconfig/readline.pc", "libedit.pc")


@subpackage("libedit-readline-devel")
def _(self):
    self.subdesc = "readline compatibility"
    self.depends = ["!readline-devel"]
    return [
        "usr/include/readline",
        "usr/lib/libhistory.*",
        "usr/lib/libreadline.*",
        "usr/lib/pkgconfig/readline.pc",
    ]


@subpackage("libedit-devel")
def _(self):
    # ncurses apk's do not provide any .pc files during stage 0
    if self.stage == 0:
        self.options = ["!scanrundeps"]
        self.depends = [self.parent, "ncurses-devel"]
    return self.default_devel()
