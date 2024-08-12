pkgname = "python-resolvelib"
pkgver = "1.0.1"
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
maintainer = "Mara <177581589+catgirlconspiracy@users.noreply.github.com>"
license = "ISC"
url = "https://github.com/sarugaku/resolvelib"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "717e92fcf64e4b7f535ebbf00d0ba21a083fa27031045af2f5040bcd38612187"


def post_install(self):
    self.install_license("LICENSE")
