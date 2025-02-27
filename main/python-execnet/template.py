pkgname = "python-execnet"
pkgver = "2.1.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Distributed python deployment and communication"
license = "MIT"
url = "https://github.com/pytest-dev/execnet"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ee16254cae42fe128acf8870002d49fe27a289c05b5b3b3c14ca4921ae74587a"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
