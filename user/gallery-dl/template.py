pkgname = "gallery-dl"
pkgver = "1.32.1"
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
sha256 = "95e69cae478cfbd407eb8451dbab9d42d65d89b861e6ee8c20888cb4b090c921"


def pre_build(self):
    self.do("make", "man", "completion")


def post_install(self):
    self.install_license("LICENSE")
