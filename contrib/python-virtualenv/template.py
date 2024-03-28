pkgname = "python-virtualenv"
pkgver = "20.25.1"
pkgrel = 0
build_style = "python_pep517"
# setuptools issue, and flaky issues
make_check_args = [
    "--deselect=tests/unit/create/via_global_ref/test_build_c_ext.py::test_can_build_c_extensions",
    "--deselect=tests/unit/seed/embed/test_bootstrap_link_via_app_data.py::test_seed_link_via_app_data",
    "--ignore=tests/integration/test_zipapp.py",
]
hostmakedepends = [
    "python-build",
    "python-filelock",
    "python-hatchling",
    "python-hatch_vcs",
    "python-installer",
    "python-platformdirs",
    "python-wheel",
]
depends = ["python-distlib", "python-platformdirs", "python-filelock"]
checkdepends = [
    "bash",
    "python-devel",
    "python-pytest",
    "python-pytest-env",
    "python-pytest-mock",
    "python-pytest-timeout",
    "python-pytest-xdist",
    "python-time-machine",
] + depends
pkgdesc = "Virtual Python Environment builder"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/pypa/virtualenv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "76bf233014b77811252f90f47fcb0330b4c5fb40c50900f0e39084986f8deff6"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
