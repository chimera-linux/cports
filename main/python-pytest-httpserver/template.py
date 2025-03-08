pkgname = "python-pytest-httpserver"
pkgver = "1.1.2"
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
sha256 = "b706af59bcf019d9d1e623b7934c316038529cb18137163289ab5387ba627d43"


def post_install(self):
    self.install_license("LICENSE")
