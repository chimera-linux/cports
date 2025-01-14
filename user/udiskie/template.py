pkgname = "udiskie"
pkgver = "2.5.7"
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/coldfix/udiskie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9a70fc97b89c03c3c70b6c87f058acd5ef2f5eb5b8158fe52738fd1cc1b61ea7"
# usr/share/zsh/site-functions/_udiskie-canonical_paths has no matching command
options = ["!lintcomp"]


def pre_check(self):
    # requires python-keyutils, unmaintained optional dep
    self.rm("test/test_cache.py")


def post_install(self):
    self.install_license("COPYING")
