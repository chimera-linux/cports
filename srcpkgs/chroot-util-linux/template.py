pkgname = "chroot-util-linux"
_mver = "2.32"
version = f"{_mver}.1"
revision = 0
wrksrc = f"util-linux-{version}"
bootstrap = True
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
makedepends = ["zlib-devel"]
short_desc = "Miscellaneous linux utilities -- for xbps-src use"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
homepage = "http://userweb.kernel.org/~kzak/util-linux-ng"

from cbuild import sites

distfiles = [
    f"{sites.kernel}/utils/util-linux/v{_mver}/util-linux-{version}.tar.xz"
]
checksum = ["86e6707a379c7ff5489c218cfaf1e3464b0b95acf7817db0bc5f179e356a67b2"]
conflicts = ["util-linux"]

def do_build(self):
    # there's something broken about the build system that sometimes
    # fails during the first pass regarding manpage generation
    try:
        self.make.build()
    except:
        self.make.build()

def post_install(self):
    # Remove unused stuff
    self.rmtree("usr/sbin")
    self.rmtree("usr/share/man")
    self.rmtree("usr/share/bash-completion")
    # Conflicts with bsdutils
    self.unlink("usr/bin/hexdump")
