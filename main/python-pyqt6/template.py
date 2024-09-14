pkgname = "python-pyqt6"
pkgver = "6.7.1"
pkgrel = 0
build_style = "makefile"
make_dir = "build"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "python-pyqt-builder",
    "python-setuptools",
    "python-sip",
]
makedepends = [
    "libx11-devel",
    "python-dbus-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebchannel-devel",
    "qt6-qtwebsockets-devel",
]
depends = ["python-pyqt6_sip"]
pkgdesc = "Python Qt6 bindings"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://www.riverbankcomputing.com/software/pyqt"
source = f"$(PYPI_SITE)/P/PyQt6/PyQt6-{pkgver}.tar.gz"
sha256 = "3672a82ccd3a62e99ab200a13903421e2928e399fda25ced98d140313ad59cb9"
# qmake needs a lot of setup to cross anything
options = ["!cross"]


def configure(self):
    self.do(
        "sip-build",
        "--confirm-license",
        "--no-make",
        "--qmake",
        "/usr/bin/qmake6",
        "--api-dir",
        "/usr/share/qt6/qsci/api/python",
        "--pep484-pyi",
        "--verbose",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
