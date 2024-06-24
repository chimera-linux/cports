pkgname = "gallery-dl"
pkgver = "1.27.1"
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
sha256 = "ffb24c82e45f773040d836e9be3ebf4463842bac44ad979655286946b5ad926e"


def pre_build(self):
    self.do("gmake", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
