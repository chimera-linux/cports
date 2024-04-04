pkgname = "libedit"
pkgver = "20230530"
pkgrel = 0
_gitrev = "bcf25b69b1a52b9b9b33c17e742f429983e30b9d"
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "c27333d42900ce01b970c8038764b80ea65838d1a08b301e86e8ea0647b3562e"
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
def _rldevel(self):
    self.pkgdesc = f"{pkgdesc} (readline compatibility)"
    self.depends = ["!readline-devel"]
    return [
        "usr/include/readline",
        "usr/lib/libhistory.*",
        "usr/lib/libreadline.*",
        "usr/lib/pkgconfig/readline.pc",
    ]


@subpackage("libedit-devel")
def _devel(self):
    # ncurses apk's do not provide any .pc files during stage 0
    if self.stage == 0:
        self.options = ["!scanrundeps"]
        self.depends = [f"libedit={pkgver}-r{pkgrel}", "ncurses-devel"]
    return self.default_devel()
