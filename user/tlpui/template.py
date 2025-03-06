pkgname = "tlpui"
pkgver = "1.8.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "cairo",
    "gtk+3",
    "python-gobject",
    "python-pyyaml",
    "tlp",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "GTK user interface for TLP"
license = "GPL-2.0-or-later"
url = "https://github.com/d4nj1/TLPUI"
source = f"{url}/archive/refs/tags/tlpui-{pkgver}.tar.gz"
sha256 = "3c1f10ac4a7bbc6041c7e57875457b916f8b312c2988c217bf9d60a19ec636ce"
