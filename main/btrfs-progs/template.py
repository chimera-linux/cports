pkgname = "btrfs-progs"
pkgver = "6.8.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-backtrace", "--enable-python"]
make_cmd = "gmake"
# build system assumes . is the root right off the bat
make_dir = "."
make_install_args = ["install_python"]
make_check_target = "test"
hostmakedepends = [
    "asciidoc",
    "automake",
    "gmake",
    "libxml2-progs",
    "pkgconf",
    "python-devel",
    "python-setuptools",
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
    "python-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.readthedocs.io/en/latest"
source = (
    f"$(KERNEL_SITE)/kernel/people/kdave/{pkgname}/{pkgname}-v{pkgver}.tar.xz"
)
sha256 = "0e40a068a26c2969cb02a95ba9fef888d7a6356e3f457ff92ad2477d08735678"
# FIXME cfi
hardening = ["vis", "!cfi"]
# non-portable testsuite assumptions, possibly FIXME
options = ["!check"]


def post_install(self):
    self.install_completion("btrfs-completion", "bash", "btrfs")


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


@subpackage("python-btrfsutil")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (python module)"
    return ["usr/lib/python*"]
