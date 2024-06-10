pkgname = "python-jsonpickle"
pkgver = "3.2.1"
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
sha256 = "4b6d7640974199f7acf9035295365b5a1a71a91109effa15ba170fbb48cf871c"


def post_install(self):
    self.install_license("LICENSE")
