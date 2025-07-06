pkgname = "python-resolvelib"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-commentjson", "python-packaging", "python-pytest"]
depends = ["python"]
pkgdesc = "Resolve abstract dependencies into concrete ones"
license = "ISC"
url = "https://github.com/sarugaku/resolvelib"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cb5858fcd2c91bd14a77654883ec64d3de309fbca349494b084c36f4ff3ff05c"


def post_install(self):
    self.install_license("LICENSE")
