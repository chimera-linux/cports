pkgname = "python-libvirt"
pkgver = "10.8.0"
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
sha256 = "10cddc61c6bc5659c0eaa3e4c71f3d97c95abf327a51c207affb2e5f49f19f60"
