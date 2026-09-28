pkgname = "python-cattrs"
pkgver = "26.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python-attrs", "python-typing_extensions"]
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
sha256 = "fa239e0f0ec0715ba34852ce813986dfed1e12117e209b816ab87401271cdd40"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--benchmark-skip",
        "--dist=worksteal",
        "--ignore=tests/strategies/test_include_subclasses.py",
        # python-immutables
        "--ignore=tests/test_cols.py",
        "--ignore=tests/test_unstructure_collections.py",
        # python-msgspec
        "--ignore=bench/test_enums.py",
        "--ignore=tests/preconf/test_msgspec_cpython.py",
        # python-bson
        "--ignore=tests/test_preconf.py",
        "--ignore=tests/preconf/test_pyyaml.py",
        # python 3.13
        "--ignore=tests/test_generics.py",
    ]


def post_install(self):
    self.install_license("LICENSE")
