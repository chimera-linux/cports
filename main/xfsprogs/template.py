pkgname = "xfsprogs"
pkgver = "6.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-editline=yes",
    "--enable-lib64=no",
]
make_cmd = "gmake"
# build system assumptions that . is the root right off the bat
make_dir = "."
# libxfs-install-dev shits itself when run in parallel
make_install_args = ["-j1", "install-dev"]
hostmakedepends = [
    "gettext-tiny", "libuuid-devel", "pkgconf", "gmake"
]
makedepends = [
    "gettext-tiny-devel", "libblkid-devel", "libedit-devel", "inih-devel",
    "userspace-rcu-devel", "linux-headers",
]
pkgdesc = "XFS file system utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://xfs.org/index.php/Main_Page"
source = f"$(KERNEL_SITE)/utils/fs/xfs/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "05e8a137870db1d6182df72dda98ab7a7100deb376947e854b9d59c914c2c7bb"
# no check target
options = ["!check"]

def init_configure(self):
    self.make_install_args += [
        f"DIST_ROOT={self.chroot_destdir}",
        "PKG_ROOT_SBIN_DIR=/usr/bin",
        "PKG_ROOT_LIB_DIR=/usr/lib"
    ]

def post_install(self):
    self.rm(self.destdir / "usr/share/doc", recursive = True)

@subpackage("xfsprogs-devel")
def _devel(self):
    self.depends += ["libuuid-devel"]

    return self.default_devel()
