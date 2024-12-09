pkgname = "python-libvirt"
pkgver = "10.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "libvirt-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = [
    "python-lxml",
    "python-pytest",
]
pkgdesc = "Libvirt virtualization API Python3 binding"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://pypi.org/project/libvirt-python"
source = f"https://libvirt.org/sources/python/libvirt-python-{pkgver}.tar.gz"
sha256 = "8acf6dcfb33a03ed92f9440cb1a0b8d3fc53fb23bba2e76ceedeb8bfb5327557"
