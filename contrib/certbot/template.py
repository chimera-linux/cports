pkgname = "certbot"
pkgver = "2.10.0"
pkgrel = 1
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
sha256 = "7e277bb461cae4071e22641e076d9232ae00ffda05bdb02832cbc1f862afab2d"


def post_install(self):
    self.install_license("LICENSE.txt")
