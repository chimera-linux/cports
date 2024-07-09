pkgname = "python-cattrs"
pkgver = "23.2.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python-attrs"]
checkdepends = [
    "python-hypothesis",
    "python-pytest-benchmark",
    "python-pytest-xdist",
] + depends
pkgdesc = "Python module for data structuring and unstructuring"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://catt.rs/en/stable"
source = f"$(PYPI_SITE)/c/cattrs/cattrs-{pkgver}.tar.gz"
sha256 = "a934090d95abaa9e911dac357e3a8699e0b4b14f8529bcc7d2b1ad9d51672b9f"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--benchmark-skip",
        "--dist=worksteal",
        # python-immutables
        "--ignore=tests/test_unstructure_collections.py",
        # python-bson
        "--ignore=tests/test_preconf.py",
    ]


def post_install(self):
    self.install_license("LICENSE")
