pkgname = "python-mako"
pkgver = "1.3.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest", "python-setuptools", "python-markupsafe"]
depends = ["python-setuptools", "python-markupsafe"]
pkgdesc = "Fast and lightweight templating engine for Python"
license = "MIT"
url = "https://www.makotemplates.org"
source = f"$(PYPI_SITE)/M/Mako/mako-{pkgver}.tar.gz"
sha256 = "99579a6f39583fa7e5630a28c3c1f440e4e97a414b80372649c0ce338da2ea28"


def post_install(self):
    self.install_license("LICENSE")
