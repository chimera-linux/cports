pkgname = "xfsprogs"
pkgver = "6.12.0"
pkgrel = 1
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
hostmakedepends = ["gettext", "util-linux-uuid-devel", "pkgconf"]
makedepends = [
    "attr-devel",
    "gettext-devel",
    "inih-devel",
    "libedit-devel",
    "linux-headers",
    "lvm2-devel",
    "userspace-rcu-devel",
    "util-linux-blkid-devel",
]
pkgdesc = "XFS file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://xfs.org/index.php/Main_Page"
source = f"$(KERNEL_SITE)/utils/fs/xfs/xfsprogs/xfsprogs-{pkgver}.tar.xz"
sha256 = "0832407247db791cc70def96e7e254bd6edf043dc84a80a62f3ccd6e3dffd329"
tool_flags = {"CFLAGS": ["-DOVERRIDE_SYSTEM_STATX"]}
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
    self.depends += ["util-linux-uuid-devel"]

    return self.default_devel()
