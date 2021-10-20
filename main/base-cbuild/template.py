pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

depends = [
    "musl-devel", "base-files", "elftoolchain", "llvm", "clang", "lld", "bmake",
    "bsdutils-extra", "dash", "file", "apk-tools-static", "awk", "ncurses",
    "bsdgrep", "bsdgzip", "bsdpatch", "bsdsed", "bsdtar", "bsddiff",
    "util-linux-cbuild", "tzdata", "mksh-static"
]
# provide a low version so it does not take over
provides = ["apk-tools=0.0.1-r0"]

options = ["bootstrap", "brokenlinks"]

if not current.bootstrapping:
    depends += ["ccache"]

def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("apk.static", "usr/bin/apk")
