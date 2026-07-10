pkgname = "nilfs-utils"
pkgver = "2.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-selinux"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "gnu-getopt",
    "linux-headers",
    "util-linux-blkid-devel",
    "util-linux-mount-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Userspace utilities for the NILFS filesystem"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://nilfs.sourceforge.io/en/index.html"
source = f"https://github.com/nilfs-dev/nilfs-utils/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4488f2978b3054fd97f87d206032cbf376d98479759d2855b57bc24a8d8efb9"
tool_flags = {
    "CFLAGS": ["-Dgetopt=gnu_getopt"],
    "LDFLAGS": ["-lgnu_getopt"],
}
options = ["etcfiles"]


@subpackage("nilfs-utils-devel")
def _(self):
    return self.default_devel()
