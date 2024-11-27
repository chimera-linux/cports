pkgname = "python-parso"
pkgver = "0.8.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Python module for parsing the Python language"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT AND PSF-2.0"
url = "https://parso.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/p/parso/parso-{pkgver}.tar.gz"
sha256 = "eb3a7b58240fb99099a345571deecc0f9540ea5f4dd2fe14c2a99d6b281ab92d"


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
