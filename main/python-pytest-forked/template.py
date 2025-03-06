pkgname = "python-pytest-forked"
pkgver = "1.6.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-py",
    "python-pytest",
]
checkdepends = [*depends]
pkgdesc = "Pytest plugin for testing parallelisation"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-forked"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "97128a8194df2c6d164b1377274a5dcfa9730f66264a48ad709e3539b25fab75"


def post_extract(self):
    # weird fnmatch behavior
    self.rm("testing/test_xfail_behavior.py")


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
