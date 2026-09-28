pkgname = "libedit"
pkgver = "20250614"
pkgrel = 0
_gitrev = "b280b361724a60fa8b740150950a59c4f4edcf15"
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "aa0fcba24403e002b3f7f6e9cf41616d8f637ce5a5708a36450f1127887f412c"
options = ["bootstrap"]


def post_install(self):
    self.install_license("COPYING")
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
