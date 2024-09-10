pkgname = "python-msgpack"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "MessagePack serializer for Python"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://msgpack.org"
source = f"https://github.com/msgpack/msgpack-python/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "336e342130db78a611f87cba9e551bc00507eb85c370549faec6109eaac7a77f"


def pre_build(self):
    # upstream seems to require manual cythonization
    # https://github.com/msgpack/msgpack-python/commit/0b1c47b06b55d91c00c9f7153c4a9440ea878886
    self.do("cython", "msgpack/_cmsgpack.pyx")
