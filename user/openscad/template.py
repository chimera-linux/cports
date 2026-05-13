pkgname = "openscad"
pkgver = "2021.01"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "bison",
    "flex",
    "gettext",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "boost-devel",
    "cgal",
    "eigen",
    "glew-devel",
    "gmp-devel",
    "libzip-devel",
    "mpfr-devel",
    "opencsg",
    "qscintilla",
    "qt6-qt5compat",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
]
pkgdesc = "Solid 3D Code CAD modeller"
license = "GPL-2.0-or-later"
url = "https://openscad.org"
source = f"https://files.openscad.org/openscad-{pkgver}.src.tar.gz"
sha256 = "d938c297e7e5f65dbab1461cac472fc60dfeaa4999ea2c19b31a4184f2d70359"


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
