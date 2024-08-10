pkgname = "gallery-dl"
pkgver = "1.27.3"
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
sha256 = "230986ed8957d8e65ea9b453df50b9bbd3fb86d0ee4b2c7ea9487db7c47aa1c7"


def pre_build(self):
    self.do("gmake", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
