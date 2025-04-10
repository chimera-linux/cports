pkgname = "python-cattrs"
pkgver = "24.1.3"
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
    *depends,
]
pkgdesc = "Python module for data structuring and unstructuring"
license = "MIT"
url = "https://catt.rs/en/stable"
source = f"$(PYPI_SITE)/c/cattrs/cattrs-{pkgver}.tar.gz"
sha256 = "981a6ef05875b5bb0c7fb68885546186d306f10f0f6718fe9b96c226e68821ff"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--benchmark-skip",
        "--dist=worksteal",
        # python-immutables
        "--ignore=tests/test_cols.py",
        "--ignore=tests/test_unstructure_collections.py",
        # python-msgspec
        "--ignore=tests/preconf/test_msgspec_cpython.py",
        # python-bson
        "--ignore=tests/test_preconf.py",
        "--ignore=tests/preconf/test_pyyaml.py",
        # python 3.13
        "--ignore=tests/test_generics.py",
    ]


def post_install(self):
    self.install_license("LICENSE")
