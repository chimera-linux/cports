pkgname = "btrfs-progs"
pkgver = "5.14.91"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-backtrace", "--disable-python"]
# build system assumes . is the root right off the bat
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake", "asciidoc", "pkgconf", "xmlto", "libxml2-progs"]
makedepends = [
    "acl-devel",
    "udev-devel",
    "libzstd-devel",
    "lzo-devel",
    "libblkid-devel",
    "libuuid-devel",
    "e2fsprogs-devel",
    "zlib-devel",
    "linux-headers",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.wiki.kernel.org/index.php/Main_Page"
source = (
    f"$(KERNEL_SITE)/kernel/people/kdave/{pkgname}/{pkgname}-v{pkgver}.tar.xz"
)
sha256 = "b8596493eab6c0107cc7547b1224dc434b39599d63e71e19f9fde33297b551bc"
# FIXME cfi
hardening = ["vis", "!cfi"]
# non-portable testsuite assumptions, possibly FIXME
options = ["!check"]


@subpackage("libbtrfs")
def _libbtrfs(self):
    self.pkgdesc = f"{pkgdesc} (btrfs library)"
    return ["usr/lib/libbtrfs.so.*"]


@subpackage("libbtrfs-devel")
def _libbtrfs_devel(self):
    self.pkgdesc = f"{pkgdesc} (libbtrfs development files)"
    return ["usr/include/btrfs", "usr/lib/libbtrfs.*"]


@subpackage("libbtrfsutil")
def _libbtrfsutil(self):
    self.pkgdesc = f"{pkgdesc} (btrfsutil library)"
    return ["usr/lib/libbtrfsutil.so.*"]


@subpackage("libbtrfsutil-devel")
def _libbtrfsutil_devel(self):
    self.pkgdesc = f"{pkgdesc} (libbtrfsutil development files)"
    return ["usr/include/btrfsutil.h", "usr/lib/libbtrfsutil.*"]


configure_gen = []
