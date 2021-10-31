pkgname = "btrfs-progs"
pkgver = "5.14.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-backtrace", "--disable-python"
]
# build system assumes . is the root right off the bat
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake", "asciidoc", "pkgconf", "xmlto", "libxml2-progs"]
makedepends = [
    "acl-devel", "libzstd-devel", "lzo-devel", "libblkid-devel",
    "libuuid-devel", "e2fsprogs-devel", "zlib-devel", "linux-headers"
]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.wiki.kernel.org/index.php/Main_Page"
source = f"$(KERNEL_SITE)/kernel/people/kdave/{pkgname}/{pkgname}-v{pkgver}.tar.xz"
sha256 = "d54a9346545ca46df128e3ccb77d60c097d90c93b7e314990236e28cfaf8c55b"
# util-linux-cbuild is incomplete
options = ["!check"]

@subpackage("libbtrfs")
def _libbtrfs(self):
    self.pkgdesc = f"{pkgdesc} (btrfs library)"
    return ["usr/lib/libbtrfs.so.*"]

@subpackage("libbtrfs-devel")
def _libbtrfs(self):
    self.pkgdesc = f"{pkgdesc} (libbtrfs development files)"
    return ["usr/include/btrfs", "usr/lib/libbtrfs.*"]

@subpackage("libbtrfsutil")
def _libbtrfsutil(self):
    self.pkgdesc = f"{pkgdesc} (btrfsutil library)"
    return ["usr/lib/libbtrfsutil.so.*"]

@subpackage("libbtrfsutil-devel")
def _libbtrfsutil(self):
    self.pkgdesc = f"{pkgdesc} (libbtrfsutil development files)"
    return ["usr/include/btrfsutil.h", "usr/lib/libbtrfsutil.*"]
