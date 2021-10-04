pkgname = "base-chroot"
pkgver = "0.1"
pkgrel = 0
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

depends = [
    "musl-devel", "base-files", "elftoolchain", "llvm", "clang", "lld", "bmake",
    "bsdutils", "dash", "file", "apk-tools", "awk", "ncurses", "bsdgrep",
    "bsdgzip", "bsdpatch", "bsdsed", "bsdtar", "bsddiff", "chroot-util-linux"
]

options = ["bootstrap", "!lint"]

if not current.bootstrapping:
    depends += ["ccache"]

def do_fetch(self):
    pass

def do_install(self):
    pass
