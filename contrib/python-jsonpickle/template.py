pkgname = "python-jsonpickle"
pkgver = "3.0.4"
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
sha256 = "a1b14c8d6221cd8f394f2a97e735ea1d7edc927fbd135b26f2f8700657c8c62b"


def post_install(self):
    self.install_license("LICENSE")
