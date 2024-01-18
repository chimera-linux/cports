pkgname = "python-blinker"
pkgver = "1.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-pytest-asyncio"]
pkgdesc = "Fast Python in-process signal/event dispatching system"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pallets-eco/blinker"
source = f"https://github.com/pallets-eco/blinker/archive/{pkgver}.tar.gz"
sha256 = "82110f6329696b99ed398a3a0e4e79206bfd34bd35fad69ec3900baa02e1342c"


def post_install(self):
    self.install_license("LICENSE.rst")
