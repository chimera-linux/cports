pkgname = "python-pytest-httpserver"
pkgver = "1.1.0"
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
sha256 = "4378ff64c5c305d7174d3f7aed9c00330c8bf6caa60ea0340885a9879aeee94d"


def post_install(self):
    self.install_license("LICENSE")
