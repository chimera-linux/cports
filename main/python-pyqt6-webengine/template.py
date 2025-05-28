pkgname = "python-pyqt6-webengine"
pkgver = "6.9.0"
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
source = f"$(PYPI_SITE)/P/PyQt6_WebEngine/pyqt6_webengine-{pkgver}.tar.gz"
sha256 = "6ae537e3bbda06b8e06535e4852297e0bc3b00543c47929541fcc9b11981aa25"


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
