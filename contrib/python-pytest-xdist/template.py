pkgname = "python-pytest-xdist"
pkgver = "3.5.0"
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
    "python-execnet",
    "python-pytest",
]
checkdepends = depends
pkgdesc = "Pytest plugin for testing parallelisation"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-xdist"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a67e623c6f87d75ed94407bbf7b084eca7b219db0bc3cc4d2ac2263d56817bef"
# unpackaged filelock
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
