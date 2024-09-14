pkgname = "python-jedi"
pkgver = "0.19.1"
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
sha256 = "cf0496f3651bc65d7174ac1b7d043eff454892c708a87d1b683e57b569927ffd"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
