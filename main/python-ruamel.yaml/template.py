pkgname = "python-ruamel.yaml"
pkgver = "0.18.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-ruamel.yaml.clib"]
checkdepends = ["python-pytest"]
pkgdesc = "YAML parser/emitter for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://sourceforge.net/projects/ruamel-yaml"
source = f"$(PYPI_SITE)/r/ruamel.yaml/ruamel.yaml-{pkgver}.tar.gz"
sha256 = "20c86ab29ac2153f80a428e1254a8adf686d3383df04490514ca3b79a362db58"
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
