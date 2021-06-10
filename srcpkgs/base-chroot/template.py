pkgname = "base-chroot"
version = "0.66"
revision = 4
bootstrap = True
short_desc = "Minimal set of packages required for chroot with xbps-src"
maintainer = "Juan RP <xtraeme@gmail.com>"
license = "Public Domain"
homepage = "http://www.voidlinux.org"

depends = [
    "musl-devel", "base-files", "binutils", "gcc", "patch", "sed", "findutils",
    "diffutils", "make", "gzip", "coreutils", "file", "bsdtar", "xbps",
    "ncurses", "bsdgrep", "chroot-bash", "chroot-gawk", "chroot-git",
    "chroot-util-linux"
]

def do_fetch(self):
    pass

def do_install(self):
    pass
