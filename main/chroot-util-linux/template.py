pkgname = "chroot-util-linux"
_mver = "2.32"
pkgver = f"{_mver}.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-ncurses", "--without-ncursesw", "--without-udev",
    "--without-systemd", "--disable-libuuid", "--disable-libblkid",
    "--disable-libmount", "--disable-mount", "--disable-losetup",
    "--disable-fsck", "--disable-partx", "--disable-uuidd",
    "--disable-mountpoint", "--disable-fallocate", "--disable-unshare",
    "--disable-nls", "--disable-wall", "--disable-chfn-chsh-password",
    "--disable-su", "--disable-sulogin", "--disable-login",
    "--disable-runuser", "--disable-setpriv", "--disable-libsmartcols",
    "--without-readline", "scanf_cv_alloc_modifier=as"
]
make_cmd = "gmake"
makedepends = ["zlib-devel"]
depends = ["!util-linux"]
pkgdesc = "Miscellaneous linux utilities (for cbuild use)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
homepage = "http://userweb.kernel.org/~kzak/util-linux-ng"

options = ["bootstrap", "!check"]

if not current.bootstrapping:
	hostmakedepends = ["gmake"]

sources = [
    f"$(KERNEL_SITE)/utils/util-linux/v{_mver}/util-linux-{pkgver}.tar.xz"
]
sha256 = ["86e6707a379c7ff5489c218cfaf1e3464b0b95acf7817db0bc5f179e356a67b2"]
conflicts = ["util-linux"]

def do_build(self):
    self.make.build()

def post_install(self):
    # Remove unused stuff
    with self.pushd(self.destdir):
        self.rm("usr/sbin", recursive = True)
        self.rm("usr/share/man", recursive = True)
        self.rm("usr/share/bash-completion", recursive = True)
        # Conflicts with bsdutils
        self.rm("usr/bin/hexdump")
