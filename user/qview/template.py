pkgname = "qview"
pkgver = "6.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = ["pkgconf", "qt6-qtbase-devel", "qt6-qttools"]
pkgdesc = "Image viewer designed with minimalism and usability in mind"
license = "GPL-3.0-or-later"
url = "https://interversehq.com/qview"
source = f"https://github.com/jurplel/qView/archive/{pkgver}.tar.gz"
sha256 = "13842c280b1bdefb7def43f6634b4153dbac3e4b51fed04ccb3b00c2b08cbe67"
hardening = ["vis", "cfi"]


def configure(self):
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]
