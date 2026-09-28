pkgname = "udiskie"
pkgver = "2.7.0"
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
    "keyutils-libs",
    "python-docopt",
    "python-gobject",
    "python-pyyaml",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Automounter for removable media"
license = "MIT"
url = "https://github.com/coldfix/udiskie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb8c173e84050db01556aad68e75cfb45fee57d880b368a395459ee5e815ce8b"
# usr/share/zsh/site-functions/_udiskie-canonical_paths has no matching command
options = ["!lintcomp"]


def pre_check(self):
    # test data breaks on loongarch
    self.rm("test/test_cache.py")


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "udiskie.user")
