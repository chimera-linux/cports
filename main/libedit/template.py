pkgname = "libedit"
pkgver = "20240711"
pkgrel = 1
_gitrev = "e75a2de6592b919b5da2384509cd3b9a5c501fe4"
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "a631168496d232ad7170cc99d9ece95f3d9202c31cdf74bd4e99c5143cd8760e"
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
