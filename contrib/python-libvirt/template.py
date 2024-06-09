pkgname = "python-libvirt"
pkgver = "10.4.0"
pkgrel = 1
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
depends = ["python"]
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
sha256 = "a20273a3374fcacb45b5ac4fd135e2c40460bb4a3a290d26c4aa8d0eaf1225b5"
