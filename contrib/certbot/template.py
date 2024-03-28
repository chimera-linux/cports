pkgname = "certbot"
pkgver = "2.9.0"
pkgrel = 0
build_wrksrc = "certbot"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-acme",
    "python-configargparse",
    "python-configobj",
    "python-cryptography",
    "python-distro",
    "python-josepy",
    "python-parsedatetime",
]
checkdepends = [
    "python-pytest",
] + depends
pkgdesc = "Tool to obtain certs from Let's Encrypt"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0 AND MIT"
url = "https://github.com/certbot/certbot"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ea80efe949bcf95c1a0b5ac77024e700c89b44f0b5a078d5bea5f673bef9eee3"


def post_install(self):
    self.install_license("LICENSE.txt")
