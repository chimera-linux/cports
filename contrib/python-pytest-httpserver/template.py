pkgname = "python-pytest-httpserver"
pkgver = "1.0.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-werkzeug"]
checkdepends = depends + ["python-pytest", "python-requests"]
pkgdesc = "Pytest http server extension"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/csernazs/pytest-httpserver"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dc9e22b54184a9683a57eb18527dae4411fed3c5b421c52521043c192d058c9b"


def post_install(self):
    self.install_license("LICENSE")
