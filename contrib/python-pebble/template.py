pkgname = "python-pebble"
pkgver = "5.0.3"
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
sha256 = "c85b91ab752900c9a857a7ecd8981a5efa41918e50a4b52c20e69964b3d3dac3"
