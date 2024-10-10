pkgname = "python-linux-procfs"
pkgver = "0.7.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-six",
]
pkgdesc = "Python bindings for the linux procfs filesystem"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/libs/python/python-linux-procfs/python-linux-procfs.git"
source = f"{url}/snapshot/python-linux-procfs-{pkgver}.tar.gz"
sha256 = "a8750f07f6b1a4c1cda6c50a33af9dc92a1a9c6cf538fd269c0db8d4c93d8ede"
# check: test is invalid using pytest
options = ["!check"]
