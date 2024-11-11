pkgname = "python-jedi"
pkgver = "0.19.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-parso"]
checkdepends = [
    "python-attrs",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Autocompletion and analysis library for Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://jedi.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/j/jedi/jedi-{pkgver}.tar.gz"
sha256 = "4770dc3de41bde3966b02eb84fbcf557fb33cce26ad23da12c742fb50ecb11f0"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
