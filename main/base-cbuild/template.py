pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

depends = [
    "base-files", "musl-devel", "elftoolchain", "llvm", "clang", "lld",
    "apk-tools-static", "bsdutils-extra", "bsdgrep", "bsdgzip", "bsdpatch",
    "bsdsed", "bsddiff", "bmake", "bsdtar", "dash", "mksh-static", "awk",
    "ncurses", "util-linux-cbuild", "tzdata", "fakeroot",
]
# provide a low version so it does not take over
provides = ["apk-tools=0.0.1-r0"]

options = ["bootstrap", "brokenlinks"]

if current.stage > 1:
    depends += ["ccache"]

def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("apk.static", "usr/bin/apk")
