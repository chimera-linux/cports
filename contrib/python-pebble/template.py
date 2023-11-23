pkgname = "python-pebble"
pkgver = "5.0.4"
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
sha256 = "287dbeec66f3340a7592cba94f03743386f00fa31063d82b6585c54f2885087a"
