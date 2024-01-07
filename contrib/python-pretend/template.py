pkgname = "python-pretend"
pkgver = "1.0.9"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Stubbing helper for python"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/alex/pretend"
source = f"https://github.com/alex/pretend/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "890313320280455daeaa11100e8b765093fee7839ae946de38333601fe544a16"


def post_install(self):
    self.install_license("LICENSE.rst")
