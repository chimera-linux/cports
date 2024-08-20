pkgname = "xfsprogs"
pkgver = "6.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-editline=yes",
    "--enable-lib64=no",
]
# regenerated configure breaks the build
configure_gen = []
make_cmd = "gmake"
# build system assumptions that . is the root right off the bat
make_dir = "."
# libxfs-install-dev shits itself when run in parallel
make_install_args = ["-j1", "install-dev"]
hostmakedepends = ["gettext", "libuuid-devel", "pkgconf", "gmake"]
makedepends = [
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
sha256 = "975284783fb3fbc4e1ae640bd804d788e4237a86b07582acee86b6e48f6521b7"
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


@subpackage("xfsprogs-devel")
def _(self):
    self.depends += ["libuuid-devel"]

    return self.default_devel()
