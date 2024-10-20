pkgname = "python-ruamel.yaml.clib"
pkgver = "0.2.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "C interface for ruamel.yaml"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sourceforge.net/projects/ruamel-yaml-clib"
source = f"$(PYPI_SITE)/r/ruamel.yaml.clib/ruamel.yaml.clib-{pkgver}.tar.gz"
sha256 = "e99304a75481da179163d5b9b841fc20dc8b99ff62b13081e474b278e15362f3"
# abysmal vendored libyaml
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
