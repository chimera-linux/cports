pkgname = "python-blinker"
pkgver = "1.8.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-pytest-asyncio"]
pkgdesc = "Fast Python in-process signal/event dispatching system"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pallets-eco/blinker"
source = f"https://github.com/pallets-eco/blinker/archive/{pkgver}.tar.gz"
sha256 = "8bdbf175087cf3af2c5b13ad247cf832ad03f93daceffff7cbaaae95b63d9581"


def post_install(self):
    self.install_license("LICENSE.txt")
