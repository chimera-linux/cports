pkgname = "qalculate-qt"
# match to libqalculate
pkgver = "5.12.0"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "qt6-qtbase-devel",
    "qt6-qttools",
]
makedepends = [
    "libqalculate-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt frontend for libqalculate"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/qalculate-qt/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "be460b472585a20a95754ff35495b179438a581af37708b49d28cb93f441c461"


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
