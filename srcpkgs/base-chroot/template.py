pkgname = "base-chroot"
version = "0.66"
revision = 5
bootstrap = True
short_desc = "Minimal set of packages required for chroot with xbps-src"
maintainer = "Juan RP <xtraeme@gmail.com>"
license = "Public Domain"
homepage = "http://www.voidlinux.org"

depends = [
    "musl-devel", "base-files", "binutils", "gcc", "diffutils", "bmake",
    "bsdutils", "coreutils", "dash", "file", "xbps", "apk-tools", "awk",
    "ncurses", "bsdgrep", "bsdgzip", "bsdpatch", "bsdsed", "bsdtar",
    "chroot-util-linux"
]

def do_fetch(self):
    pass

def do_install(self):
    pass
