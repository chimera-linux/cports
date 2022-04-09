pkgname = "util-linux-cbuild"
pkgver = "2.38"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-ncurses", "--without-ncursesw", "--without-udev",
    "--without-systemd", "--disable-libuuid", "--disable-libblkid",
    "--disable-libmount", "--disable-mount", "--disable-losetup",
    "--disable-fsck", "--disable-partx", "--disable-uuidd",
    "--disable-mountpoint", "--disable-fallocate",
    "--disable-nls", "--disable-wall", "--disable-chfn-chsh-password",
    "--disable-su", "--disable-sulogin", "--disable-login",
    "--disable-runuser", "--disable-setpriv", "--disable-libsmartcols",
    "--without-readline", "scanf_cv_alloc_modifier=as"
]
make_cmd = "gmake"
makedepends = ["zlib-devel"]
depends = ["!util-linux"]
pkgdesc = "Cbuild container version of util-linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://mirrors.edge.kernel.org/pub/linux/utils/util-linux"
source = f"$(KERNEL_SITE)/utils/util-linux/v{pkgver}/util-linux-{pkgver}.tar.xz"
sha256 = "6d111cbe4d55b336db2f1fbeffbc65b89908704c01136371d32aa9bec373eb64"
# test suite needs bash
options = ["bootstrap", "!check"]

if self.stage > 0:
    hostmakedepends = ["gmake"]
    makedepends += ["linux-headers"]

def post_install(self):
    # Remove unused stuff
    with self.pushd(self.destdir):
        self.rm("usr/sbin", recursive = True)
        self.rm("usr/share/man", recursive = True)
        self.rm("usr/share/bash-completion", recursive = True)
        # Conflicts with bsdutils
        self.rm("usr/bin/hexdump")
