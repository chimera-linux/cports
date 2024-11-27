pkgname = "python-btrfs"
pkgver = "14.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Python module and utilities for interacting with btrfs filesystems"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/knorrie/python-btrfs"
source = f"$(PYPI_SITE)/b/btrfs/btrfs-{pkgver}.tar.gz"
sha256 = "04f28fc13df78bc7d060991465b9c9f2740d6e62b0d03aba7a46fd9abedac046"
# no tests
options = ["!check"]
