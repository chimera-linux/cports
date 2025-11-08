pkgname = "tlpui"
pkgver = "1.8.1"
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
sha256 = "658f3dcfa8ea080226dd2ec1419868fe195514aeac2b1ec8f4a8d2a4546ee2de"
