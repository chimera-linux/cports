pkgname = "python-filelock"
pkgver = "3.18.0"
pkgrel = 1
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
license = "Unlicense"
url = "https://github.com/tox-dev/filelock"
source = f"$(PYPI_SITE)/f/filelock/filelock-{pkgver}.tar.gz"
sha256 = "adbc88eabb99d2fec8c9c1b229b171f18afa655400173ddc653d5d01501fb9f2"
# missing check dependencies
options = ["!check"]
