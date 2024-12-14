pkgname = "python-pyqt6-webengine"
pkgver = "6.8.0"
pkgrel = 0
build_style = "makefile"
make_dir = "build"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "python",
    "python-pyqt-builder",
    "python-pyqt6",
    "python-setuptools",
    "python-sip",
]
makedepends = [
    "python-devel",
    "python-pyqt6",
    "qt6-qtbase-devel",
    "qt6-qtwebchannel-devel",
    "qt6-qtwebengine-devel",
]
depends = ["python-pyqt6"]
pkgdesc = "Python bindings for QtWebengine"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://pypi.org/project/PyQt6-WebEngine"
source = f"$(PYPI_SITE)/P/PyQt6_WebEngine/PyQt6_WebEngine-{pkgver}.tar.gz"
sha256 = "64045ea622b6a41882c2b18f55ae9714b8660acff06a54e910eb72822c2f3ff2"


def configure(self):
    self.do(
        "sip-build",
        "--no-make",
        "--qmake",
        "/usr/bin/qmake6",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
