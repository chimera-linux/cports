pkgname = "qutebrowser"
pkgver = "3.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "asciidoc",
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "pdfjs",
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
license = "GPL-3.0-only"
url = "https://qutebrowser.org"
source = f"https://github.com/qutebrowser/qutebrowser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fb61c84bf3590e5f44f94b65d491b74b95eafb0e0ffd45b93565152c547b45c8"
# not worth it
options = ["!check"]


def post_install(self):
    self.do(
        "make",
        "-f",
        "misc/Makefile",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
        "install",
    )
