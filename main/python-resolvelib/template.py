pkgname = "python-resolvelib"
pkgver = "1.1.0"
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
sha256 = "660e2cef5342adfcdf2144539b4bfcba660682db3a8f3feb31d9ff153af8c461"


def post_install(self):
    self.install_license("LICENSE")
