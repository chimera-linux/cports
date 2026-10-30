pkgname = "beancount"
pkgver = "3.2.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "bison",
    "flex",
    "meson",
    "pkgconf",
    "python-build",
    "python-devel",
    "python-installer",
    "python-meson",
]
depends = [
    "python-click",
    "python-dateutil",
    "python-regex",
]
checkdepends = [
    "gnupg",
    "python-pytest",
    *depends,
]
pkgdesc = "Double-entry accounting from text files"
license = "GPL-2.0-only"
url = "https://github.com/beancount/beancount"
source = f"$(PYPI_SITE)/b/beancount/beancount-{pkgver}.tar.gz"
sha256 = "f52c4d237bcb092cbf02a29373d3e59d95349c2828a91491818ae437ee220f74"


def pre_check(self):
    self.mv("beancount", "tests")


def post_install(self):
    self.install_license("COPYING")
