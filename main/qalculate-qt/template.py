pkgname = "qalculate-qt"
# match to libqalculate
pkgver = "5.5.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/qalculate-qt/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "63090e557d21650ec5e11798f1e0d3bbe6bf33a3e7d0a7a2d48d778c92f947fa"


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]
