pkgname = "python-jsonpickle"
pkgver = "4.0.0"
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
    # "python-pandas",
    "python-pytest",
]
pkgdesc = "Serializing any arbitrary object graph into JSON"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/jsonpickle/jsonpickle"
source = f"$(PYPI_SITE)/j/jsonpickle/jsonpickle-{pkgver}.tar.gz"
sha256 = "fc670852b204d77601b08f8f9333149ac37ab6d3fe4e6ed3b578427291f63736"


def post_install(self):
    self.install_license("LICENSE")
