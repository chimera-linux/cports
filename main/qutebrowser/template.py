pkgname = "qutebrowser"
pkgver = "3.3.1"
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
sha256 = "83d3a3b192f4329c94e5664047de847e33649b2969f459de9b519aed18c26cbd"
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
