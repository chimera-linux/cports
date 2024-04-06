pkgname = "python-execnet"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-hatch_vcs",
    "python-hatchling",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Distributed python deployment and communication"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pytest-dev/execnet"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96d55913d3dc1a611a1600aeeaed0a4bb1fa6db0490842acd6ddd2f2624f5cd3"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
