pkgname = "btrfs-progs"
pkgver = "6.17"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-backtrace", "--enable-python"]
# build system assumes . is the root right off the bat
make_dir = "."
make_install_args = ["install_python"]
make_check_target = "test"
hostmakedepends = [
    "asciidoc",
    "automake",
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
    "linux-headers",
    "lzo-devel",
    "python-devel",
    "udev-devel",
    "util-linux-blkid-devel",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["xz"]
pkgdesc = "Btrfs file system utilities"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "https://btrfs.readthedocs.io/en/latest"
source = f"$(KERNEL_SITE)/kernel/people/kdave/btrfs-progs/btrfs-progs-v{pkgver}.tar.xz"
sha256 = "277d696c9d79713ff5afb53c7efebdcead2e6a6007789b1742ec411f4e4ca229"
hardening = ["vis", "!cfi"]
# non-portable testsuite assumptions, possibly FIXME
options = ["!check"]


def post_install(self):
    self.install_completion("btrfs-completion", "bash", "btrfs")


@subpackage("btrfs-progs-libs")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libbtrfs"),
        self.with_pkgver("libbtrfsutil"),
    ]

    return self.default_libs()


@subpackage("btrfs-progs-devel")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libbtrfs-devel"),
        self.with_pkgver("libbtrfsutil-devel"),
    ]

    return self.default_devel()


@subpackage("btrfs-progs-python")
def _(self):
    self.subdesc = "python module"
    # transitional
    self.provides = [self.with_pkgver("python-btrfsutil")]
    self.depends += ["python"]

    return ["usr/lib/python*"]
