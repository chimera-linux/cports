pkgname = "python-jedi"
pkgver = "0.20.0"
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
license = "MIT"
url = "https://jedi.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/j/jedi/jedi-{pkgver}.tar.gz"
sha256 = "c3f4ccbd276696f4b19c54618d4fb18f9fc24b0aef02acf704b23f487daa1011"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
