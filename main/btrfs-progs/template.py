pkgname = "btrfs-progs"
pkgver = "6.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-backtrace", "--disable-python"]
make_cmd = "gmake"
# build system assumes . is the root right off the bat
make_dir = "."
make_check_target = "test"
hostmakedepends = [
    "asciidoc",
    "automake",
    "gmake",
    "libxml2-progs",
    "pkgconf",
    "python-sphinx",
    "python-sphinx_rtd_theme",
    "xmlto",
]
makedepends = [
    "acl-devel",
    "e2fsprogs-devel",
    "libblkid-devel",
    "libuuid-devel",
    "linux-headers",
    "lzo-devel",
    "udev-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.wiki.kernel.org/index.php/Main_Page"
source = (
    f"$(KERNEL_SITE)/kernel/people/kdave/{pkgname}/{pkgname}-v{pkgver}.tar.xz"
)
sha256 = "24dc7b974f0a57ba0eca80f97440b840dfa85b0f1cb2c01bdfd97659a480b200"
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
    return [
        "usr/include/btrfsutil.h",
        "usr/lib/libbtrfsutil.*",
        "usr/lib/pkgconfig/libbtrfsutil.pc",
    ]
