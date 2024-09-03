pkgname = "python-jsonpickle"
pkgver = "3.3.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs pandas
    "--ignore=jsonpickle/ext/pandas.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-numpy",
    # "python-pandas",
    "python-pytest",
]
pkgdesc = "Serializing any arbitrary object graph into JSON"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/jsonpickle/jsonpickle"
source = f"$(PYPI_SITE)/j/jsonpickle/jsonpickle-{pkgver}.tar.gz"
sha256 = "ab467e601e5b1a1cd76f1819d014795165da071744ef30bf3786e9bc549de25a"


def post_install(self):
    self.install_license("LICENSE")
