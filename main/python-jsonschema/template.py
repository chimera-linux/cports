pkgname = "python-jsonschema"
pkgver = "4.24.0"
pkgrel = 0
build_style = "python_pep517"
# needs pip
make_check_args = ["-k", "not test_license"]
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-attrs",
    "python-jsonschema-specifications",
    "python-referencing",
    "python-rpds-py",
]
checkdepends = [
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Implementation of the JSON Schema specification for Python"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema"
source = f"$(PYPI_SITE)/j/jsonschema/jsonschema-{pkgver}.tar.gz"
sha256 = "0b4e8069eb12aedfa881333004bccaec24ecef5a8a6a4b6df142b2cc9599d196"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("COPYING")
