pkgname = "tlpui"
pkgver = "1.9.0"
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
sha256 = "88c026e16bf968d020ac7034a4978ddb51efd2f70eaf0b9e03d319696145e06c"
