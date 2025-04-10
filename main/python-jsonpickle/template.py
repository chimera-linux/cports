pkgname = "python-jsonpickle"
pkgver = "4.0.5"
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
    "python-simplejson",
    "python-pytest",
]
pkgdesc = "Serializing any arbitrary object graph into JSON"
license = "BSD-3-Clause"
url = "https://github.com/jsonpickle/jsonpickle"
source = f"$(PYPI_SITE)/j/jsonpickle/jsonpickle-{pkgver}.tar.gz"
sha256 = "f299818b39367c361b3f26bdba827d4249ab5d383cd93144d0f94b5417aacb35"


def post_install(self):
    self.install_license("LICENSE")
