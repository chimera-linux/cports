pkgname = "python-pyfuse3"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["fuse-devel", "python-devel", "linux-headers"]
depends = ["python-trio"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python bindings for libfuse"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.0-or-later"
url = "https://github.com/libfuse/pyfuse3"
source = f"{url}/releases/download/{pkgver}/pyfuse3-{pkgver}.tar.gz"
sha256 = "793493f4d5e2b3bc10e13b3421d426a6e2e3365264c24376a50b8cbc69762d39"
