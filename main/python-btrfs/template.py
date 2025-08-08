pkgname = "python-btrfs"
pkgver = "15"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Python module and utilities for interacting with btrfs filesystems"
license = "LGPL-3.0-or-later"
url = "https://github.com/knorrie/python-btrfs"
source = f"$(PYPI_SITE)/b/btrfs/btrfs-{pkgver}.tar.gz"
sha256 = "1419914ff141dfe9e16fd0477d9548d4bea733ecd77588e8cb7255ce17ada10b"
# no tests
options = ["!check"]
