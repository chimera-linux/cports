pkgname = "python-ruamel.yaml"
pkgver = "0.18.16"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-ruamel.yaml.clib"]
checkdepends = ["python-pytest"]
pkgdesc = "YAML parser/emitter for Python"
license = "MIT"
url = "https://sourceforge.net/projects/ruamel-yaml"
source = f"$(PYPI_SITE)/r/ruamel.yaml/ruamel.yaml-{pkgver}.tar.gz"
sha256 = "a6e587512f3c998b2225d68aa1f35111c29fad14aed561a26e73fab729ec5e5a"
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
