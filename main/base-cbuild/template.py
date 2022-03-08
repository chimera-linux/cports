pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

depends = [
    "base-bootstrap", "musl-devel", "elftoolchain", "llvm", "clang", "lld",
    "apk-tools", "bsdutils-extra", "bsdgzip", "bsdpatch", "bsddiff", "bmake",
    "bsdtar", "mksh-static-bin", "ncurses", "util-linux-cbuild", "tzdata",
    "fakeroot",
]

options = ["bootstrap", "brokenlinks"]

if self.stage > 1:
    depends += ["ccache", "ca-certificates"]
