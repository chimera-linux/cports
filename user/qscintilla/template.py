pkgname = "qscintilla"
pkgver = "2.14.1"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "qt6-qtbase",
]
makedepends = [
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Qt text/code editor library"
license = "GPL-3.0-only"
url = "https://www.riverbankcomputing.com/software/qscintilla/intro"
source = f"https://www.riverbankcomputing.com/static/Downloads/QScintilla/{pkgver}/QScintilla_src-{pkgver}.tar.gz"
sha256 = "dfe13c6acc9d85dfcba76ccc8061e71a223957a6c02f3c343b30a9d43a4cdd4d"


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
        env={"QMAKEFEATURES": "features"},
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]
