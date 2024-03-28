pkgname = "python-acme"
pkgver = "2.9.0"
pkgrel = 0
build_wrksrc = "acme"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
]
depends = [
    "python-cryptography",
    "python-josepy",
    "python-openssl",
    "python-pytz",
    "python-requests",
    "python-pyrfc3339",
]
checkdepends = [
    "python-pytest",
] + depends
pkgdesc = "ACME protocol implementation"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/certbot/acme"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ea80efe949bcf95c1a0b5ac77024e700c89b44f0b5a078d5bea5f673bef9eee3"


def post_install(self):
    self.install_license("LICENSE.txt")
