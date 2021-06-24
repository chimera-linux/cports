pkgname = "base-chroot"
version = "0.66"
revision = 5
bootstrap = True
short_desc = "Core package set for cbuild containers"
maintainer = "q66 <daniel@octaforge.org>"
license = "Public Domain"
homepage = "https://chimera-linux.org"

depends = [
    "musl-devel", "base-files", "elftoolchain", "clang", "lld", "diffutils",
    "bmake", "bsdutils", "coreutils", "dash", "file", "apk-tools", "awk",
    "ncurses", "bsdgrep", "bsdgzip", "bsdpatch", "bsdsed", "bsdtar",
    "chroot-util-linux"
]

def do_fetch(self):
    pass

def do_install(self):
    pass
