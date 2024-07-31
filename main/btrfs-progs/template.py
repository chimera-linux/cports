pkgname = "btrfs-progs"
pkgver = "6.10"
pkgrel = 0
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
    "python-devel",
    "udev-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.readthedocs.io/en/latest"
source = f"$(KERNEL_SITE)/kernel/people/kdave/btrfs-progs/btrfs-progs-v{pkgver}.tar.xz"
sha256 = "3382a84e3fcfe1ffdea07a61ab3f4e86665d38fa35f1f34548d5df867423e0df"
hardening = ["vis", "!cfi"]
# non-portable testsuite assumptions, possibly FIXME
# libbtrfsutils/python broken on cross
options = ["!check", "!cross"]


def post_install(self):
    self.install_completion("btrfs-completion", "bash", "btrfs")


@subpackage("libbtrfs")
def _libbtrfs(self):
    self.subdesc = "btrfs library"
    return ["usr/lib/libbtrfs.so.*"]


@subpackage("libbtrfs-devel")
def _libbtrfs_devel(self):
    self.subdesc = "libbtrfs development files"
    return ["usr/include/btrfs", "usr/lib/libbtrfs.*"]


@subpackage("libbtrfsutil")
def _libbtrfsutil(self):
    self.subdesc = "btrfsutil library"
    return ["usr/lib/libbtrfsutil.so.*"]


@subpackage("libbtrfsutil-devel")
def _libbtrfsutil_devel(self):
    self.subdesc = "libbtrfsutil development files"
    return [
        "usr/include/btrfsutil.h",
        "usr/lib/libbtrfsutil.*",
        "usr/lib/pkgconfig/libbtrfsutil.pc",
    ]


@subpackage("python-btrfsutil")
def _python(self):
    self.subdesc = "python module"
    self.depends += ["python"]
    return ["usr/lib/python*"]
