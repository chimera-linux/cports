pkgname = "python-filelock"
pkgver = "3.13.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Platform-independent file lock for Python"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "Unlicense"
url = "https://github.com/tox-dev/filelock"
source = f"$(PYPI_SITE)/f/filelock/filelock-{pkgver}.tar.gz"
sha256 = "d13f466618bfde72bd2c18255e269f72542c6e70e7bac83a0232d6b1cc5c8cf4"
# missing check dependencies
options = ["!check"]
