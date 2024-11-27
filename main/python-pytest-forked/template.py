pkgname = "python-pytest-forked"
pkgver = "1.6.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-pytest",
]
checkdepends = [*depends]
pkgdesc = "Pytest plugin for testing parallelisation"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-forked"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "97128a8194df2c6d164b1377274a5dcfa9730f66264a48ad709e3539b25fab75"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
