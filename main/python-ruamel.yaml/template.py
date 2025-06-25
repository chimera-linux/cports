pkgname = "python-ruamel.yaml"
pkgver = "0.18.14"
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
sha256 = "7227b76aaec364df15936730efbf7d72b30c0b79b1d578bbb8e3dcb2d81f52b7"
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
