pkgname = "python-pint"
pkgver = "0.24.4"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--benchmark-skip",
    "--deselect=pint/testsuite/test_quantity.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-flexcache",
    "python-flexparser",
    "python-platformdirs",
]
checkdepends = [
    *depends,
    "python-pytest",
    "python-pytest-benchmark",
    "python-pytest-subtests",
]
pkgdesc = "Physical quantities module"
license = "BSD-3-Clause"
url = "https://github.com/hgrecco/pint"
source = f"$(PYPI_SITE)/p/pint/pint-{pkgver}.tar.gz"
sha256 = "35275439b574837a6cd3020a5a4a73645eb125ce4152a73a2f126bf164b91b80"


def post_install(self):
    self.install_license("LICENSE")
