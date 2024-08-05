pkgname = "gallery-dl"
pkgver = "1.27.2"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs internet
    "--deselect=test/test_results.py",
]
hostmakedepends = [
    "gmake",
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-requests"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "CLI program to download image galleries/collections"
maintainer = "Nasado <hi@nasado.name>"
license = "GPL-2.0-or-later"
url = "https://github.com/mikf/gallery-dl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b47201ef99f72a9b5404faf9b3703378a90b4c41efd93967e40c16f303eef8ca"


def pre_build(self):
    self.do("gmake", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
