pkgname = "python-dunamai"
pkgver = "1.26.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-poetry-core"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Dynamic versioning library and cli"
license = "MIT"
url = "https://github.com/mtkennerly/dunamai"
source = f"$(PYPI_SITE)/d/dunamai/dunamai-{pkgver}.tar.gz"
sha256 = "3b46007bd65b00b4824ead0a1aee365fd22d0ec2b9c219497d4fd48f52860c8b"
# needs VCS to perform test
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
