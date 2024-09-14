pkgname = "python-ruamel.yaml.clib"
pkgver = "0.2.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "C interface for ruamel.yaml"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sourceforge.net/projects/ruamel-yaml-clib"
source = f"$(PYPI_SITE)/r/ruamel.yaml.clib/ruamel.yaml.clib-{pkgver}.tar.gz"
sha256 = "beb2e0404003de9a4cab9753a8805a8fe9320ee6673136ed7f04255fe60bb512"
# abysmal vendored libyaml
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
