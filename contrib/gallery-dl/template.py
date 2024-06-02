pkgname = "gallery-dl"
pkgver = "1.27.0"
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
    "python-wheel",
]
depends = ["python-requests"]
checkdepends = ["python-pytest"] + depends
pkgdesc = (
    "CLI program to download image galleries and collections from many sites"
)
maintainer = "Nasado <hi@nasado.name>"
license = "GPL-2.0-or-later"
url = "https://github.com/mikf/gallery-dl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6fc7ed21b0fcb858dd457d972499ae6b7aab86e8888753606df3096d8dc501cd"


def pre_build(self):
    self.do("gmake", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
