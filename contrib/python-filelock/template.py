pkgname = "python-filelock"
pkgver = "3.13.3"
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
sha256 = "a79895a25bbefdf55d1a2a0a80968f7dbb28edcd6d4234a0afb3f37ecde4b546"
# missing check dependencies
options = ["!check"]
