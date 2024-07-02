pkgname = "python-jaraco.functools"
pkgver = "4.0.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--deselect=test_functools.py"]  # unpackaged deps
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-more-itertools"]
checkdepends = depends + [
    "python-pytest",
    "python-jaraco.classes",
]
pkgdesc = "Functools like those found in stdlib"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/jaraco.functools"
source = f"$(PYPI_SITE)/j/jaraco_functools/jaraco_functools-{pkgver}.tar.gz"
sha256 = "d33fa765374c0611b52f8b3a795f8900869aa88c84769d4d1746cd68fb28c3e8"


def post_install(self):
    self.install_license("LICENSE")
