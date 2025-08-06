pkgname = "python-pebble"
pkgver = "5.1.3"
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
sha256 = "8304af95d4d43d73c4f648403114be8cefcb9527d27488bb9e974ea6cde2661a"
