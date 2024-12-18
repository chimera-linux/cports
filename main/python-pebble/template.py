pkgname = "python-pebble"
pkgver = "5.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Multi-threading and processing for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/noxdafox/pebble"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d4b9bd857fe34b287e522fd2f206e53b495b4650d57837fe4fa8c8c5b854c668"
