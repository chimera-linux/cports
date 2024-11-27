pkgname = "python-ruamel.yaml"
pkgver = "0.18.6"
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
sha256 = "8b27e6a217e786c6fbe5634d8f3f11bc63e0f80f6a5890f28863d9c45aac311b"
# no tests on pypi
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
