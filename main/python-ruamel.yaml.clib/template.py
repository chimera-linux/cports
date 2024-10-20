pkgname = "python-ruamel.yaml.clib"
pkgver = "0.2.12"
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
sha256 = "6c8fbb13ec503f99a91901ab46e0b07ae7941cd527393187039aec586fdfd36f"
# abysmal vendored libyaml
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
