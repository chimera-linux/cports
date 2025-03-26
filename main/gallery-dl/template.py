pkgname = "gallery-dl"
pkgver = "1.29.2"
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
sha256 = "0ce5138cec365f658dfeb4df7250423e42837d5c4ea970a5d65c4940f2f27fa3"


def pre_build(self):
    self.do("make", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
