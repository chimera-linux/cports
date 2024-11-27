pkgname = "python-u-msgpack"
pkgver = "2.8.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python msgpack serializer and deserializer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/vsergeev/u-msgpack-python"
source = f"$(PYPI_SITE)/u/u-msgpack-python/u-msgpack-python-{pkgver}.tar.gz"
sha256 = "b801a83d6ed75e6df41e44518b4f2a9c221dc2da4bcd5380e3a0feda520bc61a"


def post_install(self):
    self.install_license("LICENSE")
