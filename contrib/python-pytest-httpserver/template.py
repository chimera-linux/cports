pkgname = "python-pytest-httpserver"
pkgver = "1.0.12"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-werkzeug"]
checkdepends = ["python-pytest", "python-requests", *depends]
pkgdesc = "Pytest http server extension"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/csernazs/pytest-httpserver"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a265290e659458bd187952fd8f3ce66520ca08146a0ce062bc390d18bc5e3174"


def post_install(self):
    self.install_license("LICENSE")
