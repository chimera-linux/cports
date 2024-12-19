pkgname = "udiskie"
pkgver = "2.5.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "asciidoc",
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "libnotify",
    "python-docopt",
    "python-gobject",
    "python-pyyaml",
    "udisks",
]
pkgdesc = "Automounter for removable media"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "MIT"
url = "https://github.com/coldfix/udiskie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6971adaa00dcd6b799b8a0b62c47103e0ad9a3f1880112c51ccc662316d2b306"
# check: tests depend on python-keyutils 0.3 (super old)
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "50-udiskie.rules", "usr/share/polkit-1/rules.d"
    )
    self.uninstall("usr/share/zsh/site-functions/_udiskie-canonical_paths")
