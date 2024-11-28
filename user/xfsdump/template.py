pkgname = "xfsdump"
pkgver = "3.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-lib64=no"]
# autoheader breaks definitions in include/config.h.in
configure_gen = []
# build system expects to be in the root of the source directory
make_dir = "."
make_install_args = ["PKG_ROOT_SBIN_DIR=/usr/bin"]
hostmakedepends = ["gettext"]
makedepends = ["attr-devel", "linux-headers", "ncurses-devel", "xfsprogs-devel"]
pkgdesc = "XFS dump tools"
maintainer = "nilfsuser5678 <chimera-dev.o6dyz@passmail.net>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/fs/xfs/xfsdump-dev.git"
source = f"$(KERNEL_SITE)/utils/fs/xfs/xfsdump/xfsdump-{pkgver}.tar.xz"
sha256 = "2914dbbe1ebc88c7d93ad88e220aa57dabc43d216e11f06221c01edf3cc10732"
# there are asserts that dont compile when DEBUG isn't defined so they need to be disabled
tool_flags = {"CFLAGS": ["-DNDEBUG", "-D_LARGEFILE64_SOURCE"]}
# there is no make check
options = ["!check"]


def post_install(self):
    # the docs are useless
    self.uninstall("usr/share/doc/xfsdump")
