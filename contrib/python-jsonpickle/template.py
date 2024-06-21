pkgname = "python-jsonpickle"
pkgver = "3.2.2"
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
sha256 = "d425fd2b8afe9f5d7d57205153403fbf897782204437882a477e8eed60930f8c"


def post_install(self):
    self.install_license("LICENSE")
