pkgname = "python-filelock"
pkgver = "3.29.0"
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
license = "Unlicense"
url = "https://github.com/tox-dev/filelock"
source = f"$(PYPI_SITE)/f/filelock/filelock-{pkgver}.tar.gz"
sha256 = "69974355e960702e789734cb4871f884ea6fe50bd8404051a3530bc07809cf90"
# missing check dependencies
options = ["!check"]
