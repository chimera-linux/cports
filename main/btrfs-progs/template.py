pkgname = "btrfs-progs"
pkgver = "6.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-backtrace", "--disable-python"]
configure_gen = []
# build system assumes . is the root right off the bat
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = [
    "asciidoc",
    "gmake",
    "libxml2-progs",
    "pkgconf",
    "python-sphinx",
    "xmlto",
]
makedepends = [
    "acl-devel",
    "e2fsprogs-devel",
    "libblkid-devel",
    "libuuid-devel",
    "zstd-devel",
    "linux-headers",
    "lzo-devel",
    "udev-devel",
    "zlib-devel",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.wiki.kernel.org/index.php/Main_Page"
source = (
    f"$(KERNEL_SITE)/kernel/people/kdave/{pkgname}/{pkgname}-v{pkgver}.tar.xz"
)
sha256 = "c558b2ddd43f5747a2f5cb62aed3e5c5099703886485a480310fed4698d3610c"
# FIXME cfi
hardening = ["vis", "!cfi"]
# non-portable testsuite assumptions, possibly FIXME
options = ["!check"]


# clang only issues a warning about unused compiler arg for -msse2 etc
if self.profile().arch != "x86_64":
    configure_args += [
        "ax_cv_check_cflags___msse2=no",
        "ax_cv_check_cflags___msse4_1=no",
        "ax_cv_check_cflags___mavx2=no",
        "ax_cv_check_cflags___msha=no",
    ]


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
