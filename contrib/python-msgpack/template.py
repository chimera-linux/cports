pkgname = "python-msgpack"
pkgver = "1.0.8"
pkgrel = 1
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
sha256 = "481996e14606bc215a8aed396c773bd4c3ae8b5afeac6622a3e02a4b33981b02"
