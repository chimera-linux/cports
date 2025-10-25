pkgname = "gallery-dl"
pkgver = "1.30.10"
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
sha256 = "e5f6c1bbf1f6478909c291042f4d763f4ba92f695d29c920bf7266fc0d65d9dc"


def pre_build(self):
    self.do("make", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
