pkgname = "qutebrowser"
pkgver = "3.4.0"
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
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://qutebrowser.org"
source = f"https://github.com/qutebrowser/qutebrowser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6b48eb5b5cdc8965564ffa259cc9c1891ef3ff62e24e64b5af7c00276ffd9098"
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
