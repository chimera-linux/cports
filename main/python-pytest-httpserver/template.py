pkgname = "python-pytest-httpserver"
pkgver = "1.1.3"
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
license = "MIT"
url = "https://github.com/csernazs/pytest-httpserver"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5ca7247206fc6d5620986cdc4fd0706046ff468165907e73d60c64fd3313674c"


def post_install(self):
    self.install_license("LICENSE")
