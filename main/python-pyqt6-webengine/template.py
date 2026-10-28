pkgname = "python-pyqt6-webengine"
pkgver = "6.140.0"
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
license = "GPL-2.0-or-later"
url = "https://pypi.org/project/PyQt6-WebEngine"
# no stable version yet for 6.140.0
# source = f"$(PYPI_SITE)/P/PyQt6_WebEngine/pyqt6_webengine-{pkgver}.tar.gz"
source = f"https://www.riverbankcomputing.com/pypi/packages/pyqt6-webengine/pyqt6_webengine-{pkgver}.tar.gz"
sha256 = "6c9090d470e3f5de30d17ce34a3002d4897079263a688dd02603b4ee8e7199a7"


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
