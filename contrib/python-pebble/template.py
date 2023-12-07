pkgname = "python-pebble"
pkgver = "5.0.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Multi-threading and processing for python"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://github.com/noxdafox/pebble"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a9e81246a6f7c61c3f9f25cdb68fa01b08df67c19c10a93b1eb993bab100e8db"
