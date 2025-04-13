pkgname = "gallery-dl"
pkgver = "1.29.3"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs internet
    "--deselect=test/test_results.py",
    "-k",
    "not test_init",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-requests"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "CLI program to download image galleries/collections"
license = "GPL-2.0-or-later"
url = "https://github.com/mikf/gallery-dl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3c604eb980189ab8a1d53d357ba3387e0b44dd1363decaa308a1d817c7d32f0b"


def pre_build(self):
    self.do("make", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
