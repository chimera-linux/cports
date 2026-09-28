pkgname = "python-parso"
pkgver = "0.8.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Python module for parsing the Python language"
license = "MIT AND PSF-2.0"
url = "https://parso.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/p/parso/parso-{pkgver}.tar.gz"
sha256 = "eaaac4c9fdd5e9e8852dc778d2d7405897ec510f2a298071453e5e3a07914bb1"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        "-k",
        # https://github.com/davidhalter/parso/issues/222
        "not test_python_exception_matches",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
