pkgname = "jinja2-cli"
pkgver = "0.8.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-jinja2"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "CLI for Jinja2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/mattrobenolt/jinja2-cli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "089f1201ed1a812cb558f15b09c74aec1885ae00bf206512e79d55cebb2858fc"


def post_install(self):
    self.install_license("LICENSE")
