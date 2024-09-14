pkgname = "python-filelock"
pkgver = "3.16.0"
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
sha256 = "81de9eb8453c769b63369f87f11131a7ab04e367f8d97ad39dc230daa07e3bec"
# missing check dependencies
options = ["!check"]
