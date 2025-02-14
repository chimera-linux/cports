pkgname = "tlpui"
pkgver = "1.7.1"
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
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "GPL-2.0-or-later"
url = "https://github.com/d4nj1/TLPUI"
source = f"{url}/archive/refs/tags/tlpui-{pkgver}.tar.gz"
sha256 = "3d94beeb34c6b89ea80e01263a5b0535421c925181782bc50c702957b4393924"
