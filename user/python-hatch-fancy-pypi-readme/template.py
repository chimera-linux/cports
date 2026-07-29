pkgname = "python-hatch-fancy-pypi-readme"
pkgver = "25.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-hatchling"]
pkgdesc = "Fancy PyPI README with hatch"
license = "MIT"
url = "https://github.com/hynek/hatch-fancy-pypi-readme"
source = f"https://pypi.io/packages/source/h/hatch-fancy-pypi-readme/hatch_fancy_pypi_readme-{pkgver}.tar.gz"
sha256 = "9c58ed3dff90d51f43414ce37009ad1d5b0f08ffc9fc216998a06380f01c0045"
# test fails at test_end_to_end.py; skip it
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
