pkgname = "qcustomplot"
pkgver = "2.1.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "qt6-qtbase-devel",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Qt widgets for plotting and data visualization"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.qcustomplot.com"
source = [
    f"{url}/release/{pkgver}/QCustomPlot-source.tar.gz",
    f"{url}/release/{pkgver}/QCustomPlot-sharedlib.tar.gz",
]
source_paths = [".", "sharedlib"]
sha256 = [
    "5e2d22dec779db8f01f357cbdb25e54fbcf971adaee75eae8d7ad2444487182f",
    "35d6ea9c7e8740edf0b37e2cb6aa6794150d0dde2541563e493f3f817012b4c0",
]
hardening = ["vis"]


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "sharedlib/sharedlib-compilation/sharedlib-compilation.pro",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def install(self):
    # no actual install in the qt .pro...
    # installing symlink files derefs the symlink so it doesn't work, relink manually
    self.install_lib(f"libqcustomplot.so.{pkgver}")
    self.install_link(
        "usr/lib/libqcustomplot.so.2.1", f"libqcustomplot.so.{pkgver}"
    )
    self.install_link("usr/lib/libqcustomplot.so.2", "libqcustomplot.so.2.1")
    self.install_link("usr/lib/libqcustomplot.so", "libqcustomplot.so.2")
    self.install_file("qcustomplot.h", "usr/include")


@subpackage("qcustomplot-devel")
def _(self):
    return self.default_devel()
