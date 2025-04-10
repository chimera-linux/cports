pkgname = "python-pebble"
pkgver = "5.1.1"
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
license = "LGPL-3.0-or-later"
url = "https://github.com/noxdafox/pebble"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8e91255f28641da9b35c906c8dda6b0a5dd57c9adedf0271cee50312708aa03a"
