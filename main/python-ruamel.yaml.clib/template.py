pkgname = "python-ruamel.yaml.clib"
pkgver = "0.2.14"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "C interface for ruamel.yaml"
license = "MIT"
url = "https://sourceforge.net/projects/ruamel-yaml-clib"
source = f"$(PYPI_SITE)/r/ruamel.yaml.clib/ruamel.yaml.clib-{pkgver}.tar.gz"
sha256 = "803f5044b13602d58ea378576dd75aa759f52116a0232608e8fdada4da33752e"
# abysmal vendored libyaml
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
