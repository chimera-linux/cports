pkgname = "python-pyfuse3"
pkgver = "3.3.0"
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
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python bindings for libfuse"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.0-or-later"
url = "https://github.com/libfuse/pyfuse3"
source = f"{url}/releases/download/{pkgver}/pyfuse3-{pkgver}.tar.gz"
sha256 = "2b31fe412479f9620da2067dd739ed23f4cc37364224891938dedf7766e573bd"
