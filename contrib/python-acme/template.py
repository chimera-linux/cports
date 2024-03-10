pkgname = "python-acme"
pkgver = "2.10.0"
pkgrel = 0
build_wrksrc = "acme"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-cryptography",
    "python-josepy",
    "python-openssl",
    "python-pyrfc3339",
    "python-pytz",
    "python-requests",
]
checkdepends = [
    "python-pytest",
] + depends
pkgdesc = "ACME protocol implementation"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/certbot/certbot/tree/master/acme"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "7e277bb461cae4071e22641e076d9232ae00ffda05bdb02832cbc1f862afab2d"


def post_install(self):
    self.install_license("LICENSE.txt")
