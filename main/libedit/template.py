pkgname = "libedit"
pkgver = "20220411"
pkgrel = 0
_gitrev = "bf6203bf7a6894bd8dc3496d1cffb48ab05b0e18"
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "80f9ee8011d94cb5b356f632af2c06d8e6b4db4716570df2e266f3d3c14f2a74"
options = ["bootstrap"]


def post_install(self):
    self.install_license("COPYING")
    # readline compat
    self.install_file(self.files_path / "readline.h", "usr/include/readline")
    self.install_file(self.files_path / "history.h", "usr/include/readline")
    self.install_file(self.files_path / "libhistory.so", "usr/lib")
    self.install_file(self.files_path / "libreadline.so", "usr/lib")
    self.install_link("libedit.a", "usr/lib/libreadline.a")
    self.install_link("libedit.a", "usr/lib/libhistory.a")
    self.install_link("libedit.pc", "usr/lib/pkgconfig/readline.pc")


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
