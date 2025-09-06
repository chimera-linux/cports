pkgname = "udiskie"
pkgver = "2.5.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-docopt",
    "python-gobject",
    "python-pyyaml",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Automounter for removable media"
license = "MIT"
url = "https://github.com/coldfix/udiskie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ade0b67392fe5cfbd3a84c502c1e76bc2edb66e3c7e1d0ccbe2e62421f699674"
# usr/share/zsh/site-functions/_udiskie-canonical_paths has no matching command
options = ["!lintcomp"]


def pre_check(self):
    # requires python-keyutils, unmaintained optional dep
    self.rm("test/test_cache.py")


def post_install(self):
    self.install_license("COPYING")
