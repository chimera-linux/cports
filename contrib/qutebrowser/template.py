pkgname = "qutebrowser"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "asciidoc",
    "gmake",
    "python",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-hypothesis",
    "python-pytest",
    "python-pytest-benchmark",
    "python-pytest-mock",
    "python-pytest-rerunfailures",
]
depends = [
    "python-adblock",
    "python-jinja2",
    "python-pygments",
    "python-pyqt6",
    "python-pyqt6-webengine",
    "python-pyqt6_sip",
    "python-pyyaml",
    "python-tldextract",
    "qt6-qtbase",
    "qt6-qtbase-dbus",
    "qt6-qtbase-sql",
    "qt6-qtwebengine",
]
pkgdesc = "Keyboard driven web browser with a minimalist gui"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://qutebrowser.org"
source = f"https://github.com/qutebrowser/qutebrowser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9307d55f1d9157b7906ac08566e3951bffd6f5b753432deaa9a13681995ba3ca"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.do(
        "gmake",
        "-f",
        "misc/Makefile",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
        "install",
    )
