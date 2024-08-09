pkgname = "python-libvirt"
pkgver = "10.6.0"
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
sha256 = "e4259cbd724f784fca9bf22b13e8af1195dead6beee4c6ea08481a66dfdc79e4"
