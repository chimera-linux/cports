pkgname = "bmaptool"
pkgver = "3.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gtar",
    "python-build",
    "python-poetry-core",
    "python-installer",
]
depends = ["gpgme-python", "gtar", "python-six"]
checkdepends = ["python-pytest", "python-six", *depends]
pkgdesc = "Tool for creating and using block maps"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/yoctoproject/bmaptool"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3c741ccdd5049b5cb6983bc186f7be8040a132ed7e9c2afda4d9e7390888163c"
