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
pkgdesc = "Keyboard driven web browser"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://qutebrowser.org"
source = f"https://github.com/qutebrowser/qutebrowser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9307d55f1d9157b7906ac08566e3951bffd6f5b753432deaa9a13681995ba3ca"
# unpackaged dependencies
options = ["!check"]


def post_build(self):
    self.do("a2x", "-f", "manpage", "doc/qutebrowser.1.asciidoc")


def post_install(self):
    self.install_man("doc/qutebrowser.1")
    self.install_dir("usr/share/qutebrowser")
    self.install_files("scripts", "usr/share/qutebrowser")
    self.install_files("misc/userscripts", "usr/share/qutebrowser")
    self.install_file(
        "misc/org.qutebrowser.qutebrowser.desktop",
        "usr/share/applications",
        name="qutebrowser.desktop",
    )
    self.install_file(
        self.files_path / "bubblejail.toml",
        "usr/share/bubblejail/profiles",
        name="qutebrowser.toml",
    )
    for i in ["16", "24", "32", "48", "64", "128", "256", "512"]:
        self.install_file(
            f"qutebrowser/icons/qutebrowser-{i}x{i}.png",
            f"usr/share/icons/hicolor/{i}x{i}/apps",
            name="qutebrowser.png",
        )
    self.install_file(
        "qutebrowser/icons/qutebrowser.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )


@subpackage("qutebrowser-bubblejail")
def _bubblejail(self):
    self.pkgdesc = f"{pkgdesc} (bubblejail profile)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "bubblejail"]

    return ["usr/share/bubblejail/profiles/qutebrowser.toml"]
