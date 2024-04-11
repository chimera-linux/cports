pkgname = "python-libvirt"
pkgver = "10.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "libvirt-devel",
    "python-devel",
]
checkdepends = [
    "python-installer",
    "python-lxml",
    "python-pytest",
]
pkgdesc = "Libvirt virtualization API Python3 binding"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://pypi.org/project/libvirt-python"
source = f"https://libvirt.org/sources/python/libvirt-python-{pkgver}.tar.gz"
sha256 = "0333781ffef915d984f36a9b475ae8df6d01763883eefbd138d14c7591f51f2f"
