pkgname = "python-python_discovery"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python-filelock", "python-platformdirs"]
checkdepends = ["python-pytest", "python-pytest-mock", *depends]
pkgdesc = "Library for finding Python interpreters"
license = "MIT"
url = "https://python-discovery.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/p/python-discovery/python_discovery-{pkgver}.tar.gz"
sha256 = "3e014c6327154d3dda27939a9a0dc9c5c000439f1906d3f303b48f984bd2ecef"


def post_install(self):
    self.install_license("LICENSE")
