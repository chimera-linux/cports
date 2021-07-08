pkgname = "base-chroot"
version = "0.66"
revision = 7
bootstrap = True
short_desc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Public Domain"
homepage = "https://chimera-linux.org"

depends = [
    "musl-devel", "base-files", "elftoolchain", "clang", "lld", "bmake",
    "bsdutils", "dash", "file", "apk-tools", "awk", "ncurses", "bsdgrep",
    "bsdgzip", "bsdpatch", "bsdsed", "bsdtar", "bsddiff", "chroot-util-linux"
]

if not current.bootstrapping:
    depends += ["ccache"]

def do_fetch(self):
    pass

def do_install(self):
    pass
