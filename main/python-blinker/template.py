pkgname = "python-blinker"
pkgver = "1.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-pytest-asyncio"]
pkgdesc = "Fast Python in-process signal/event dispatching system"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pallets-eco/blinker"
source = f"https://github.com/pallets-eco/blinker/archive/{pkgver}.tar.gz"
sha256 = "9b02df578ec0aadd5e800e5f09281e80abddab5e0f74b4b88694f06c9956b6aa"


def post_install(self):
    self.install_license("LICENSE.txt")
