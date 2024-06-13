pkgname = "python-filelock"
pkgver = "3.15.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Platform-independent file lock for Python"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "Unlicense"
url = "https://github.com/tox-dev/filelock"
source = f"$(PYPI_SITE)/f/filelock/filelock-{pkgver}.tar.gz"
sha256 = "58a2549afdf9e02e10720eaa4d4470f56386d7a6f72edd7d0596337af8ed7ad8"
# missing check dependencies
options = ["!check"]
