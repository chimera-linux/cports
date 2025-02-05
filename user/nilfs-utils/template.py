pkgname = "nilfs-utils"
pkgver = "2.2.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-selinux"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "linux-headers",
    "util-linux-blkid-devel",
    "util-linux-mount-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Userspace utilities for the NILFS filesystem"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://nilfs.sourceforge.io/en/index.html"
source = f"https://github.com/nilfs-dev/nilfs-utils/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5172adef1f4a66add0e4e2e733aef82c5b1fc2405473bcd335e516814b5f634f"


@subpackage("nilfs-utils-devel")
def _(self):
    return self.default_devel()
