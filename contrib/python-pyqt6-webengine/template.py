pkgname = "python-pyqt6-webengine"
pkgver = "6.6.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "build"
make_use_env = True
hostmakedepends = [
    "gmake",
    "python",
    "pkgconf",
    "python-pyqt-builder",
    "python-pyqt6",
    "python-sip",
]
makedepends = [
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebchannel-devel",
    "qt6-qtwebengine-devel",
    "python-pyqt6",
]
depends = ["python-pyqt6"]
pkgdesc = "Python bindings for QtWebengine"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://pypi.org/project/PyQt6-WebEngine"
source = f"$(PYPI_SITE)/P/PyQt6_WebEngine/PyQt6_WebEngine-{pkgver}.tar.gz"
sha256 = "d50b984c3f85e409e692b156132721522d4e8cf9b6c25e0cf927eea2dfb39487"


def do_configure(self):
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
