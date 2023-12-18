pkgname = "btrfs-progs"
pkgver = "6.6.3"
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
    "python-sphinx_rtd_theme",
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
sha256 = "f41ce53f6673ff551ee4a3fe7dc9601e5a0dde6b6d09177d1fab62718abc6d9a"
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
