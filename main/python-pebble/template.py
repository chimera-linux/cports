pkgname = "python-pebble"
pkgver = "5.0.7"
pkgrel = 1
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
sha256 = "ca1b85e7b65f6d993898e123528b2417e7c686760ed525cf3c8ca1c21793f658"
