pkgname = "gallery-dl"
pkgver = "1.27.4"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs internet
    "--deselect=test/test_results.py",
]
hostmakedepends = [
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
sha256 = "6f2d749d5fa2c05beefa99b0bae53a180e7a9299f9a48c307ea26b3f854e8bae"


def pre_build(self):
    self.do("make", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
