pkgname = "tlpui"
pkgver = "1.10.1"
pkgrel = 0
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
sha256 = "041b92149fdbc9e582857c386ac4d2800fb74535a16a8feb4f59398e96f554cc"
