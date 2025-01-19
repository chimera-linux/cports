pkgname = "python-libvirt"
pkgver = "11.0.0"
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
sha256 = "cee825a53c6438c5bc84b4250b35493a8e504d5d8075d3d2069ffaf7090846f8"
