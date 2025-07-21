pkgname = "python-jsonpickle"
pkgver = "4.1.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs atheris
    "--ignore=fuzzing/fuzz-targets/fuzz_unpickle.py",
    # needs pandas
    "--ignore=fuzzing/fuzz-targets/utils.py",
    "--ignore=jsonpickle/ext/pandas.py",
    "--ignore=jsonpickle/tags_pd.py",
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
    "python-pytest",
    # "python-pandas",
    "python-simplejson",
]
pkgdesc = "Serializing any arbitrary object graph into JSON"
license = "BSD-3-Clause"
url = "https://github.com/jsonpickle/jsonpickle"
source = f"$(PYPI_SITE)/j/jsonpickle/jsonpickle-{pkgver}.tar.gz"
sha256 = "f86e18f13e2b96c1c1eede0b7b90095bbb61d99fedc14813c44dc2f361dbbae1"


def post_install(self):
    self.install_license("LICENSE")
