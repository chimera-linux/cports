pkgname = "nilfs-utils"
pkgver = "2.2.12"
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://nilfs.sourceforge.io/en/index.html"
source = f"https://github.com/nilfs-dev/nilfs-utils/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6b6c0fcb3af420532192c96442133e82227012ee991a66788e7e00151ca6ee8a"


@subpackage("nilfs-utils-devel")
def _(self):
    return self.default_devel()
