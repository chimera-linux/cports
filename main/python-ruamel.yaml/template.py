pkgname = "python-ruamel.yaml"
pkgver = "0.18.11"
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
sha256 = "b586a3416676566ed45bf679a0909719f7ea7b58c03a9b6e03f905a1e2cd5076"
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
