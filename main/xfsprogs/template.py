pkgname = "xfsprogs"
pkgver = "6.11.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-editline=yes",
    "--enable-lib64=no",
]
# regenerated configure breaks the build
configure_gen = []
# build system assumptions that . is the root right off the bat
make_dir = "."
# libxfs-install-dev shits itself when run in parallel
make_install_args = ["-j1", "install-dev"]
hostmakedepends = ["gettext", "libuuid-devel", "pkgconf"]
makedepends = [
    "attr-devel",
    "device-mapper-devel",
    "gettext-devel",
    "libblkid-devel",
    "libedit-devel",
    "inih-devel",
    "userspace-rcu-devel",
    "linux-headers",
]
pkgdesc = "XFS file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://xfs.org/index.php/Main_Page"
source = f"$(KERNEL_SITE)/utils/fs/xfs/xfsprogs/xfsprogs-{pkgver}.tar.xz"
sha256 = "dae3bb432196f7b183b2e6bd5dc44bf33edbd7d0e85bd37d25c235df81b8100a"
# no check target
options = ["!check"]


def init_configure(self):
    self.make_install_args += [
        f"DIST_ROOT={self.chroot_destdir}",
        "PKG_ROOT_SBIN_DIR=/usr/bin",
        "PKG_ROOT_LIB_DIR=/usr/lib",
    ]


def post_install(self):
    self.uninstall("usr/share/doc")
    # prevents udisks automount
    self.uninstall("usr/lib/udev/rules.d/64-xfs.rules")


@subpackage("xfsprogs-devel")
def _(self):
    self.depends += ["libuuid-devel"]

    return self.default_devel()
