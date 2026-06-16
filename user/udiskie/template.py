pkgname = "udiskie"
pkgver = "2.6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["turnstile"]
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
sha256 = "9d758efd4e3706ce824e693708cce1e0a840dae9aa5b130e3592d3588da8279c"
# usr/share/zsh/site-functions/_udiskie-canonical_paths has no matching command
options = ["!lintcomp"]


def pre_check(self):
    # requires python-keyutils, unmaintained optional dep
    self.rm("test/test_cache.py")


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "udiskie.user")
