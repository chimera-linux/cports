pkgname = "qview"
pkgver = "7.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = ["pkgconf", "qt6-qtbase-devel", "qt6-qttools"]
pkgdesc = "Image viewer"
license = "GPL-3.0-or-later"
url = "https://interversehq.com/qview"
source = f"https://github.com/jurplel/qView/archive/{pkgver}.tar.gz"
sha256 = "89189b508b60526af09a15bc7b467eecb7f3d074f5dd21d251afe23406b24e8a"
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
