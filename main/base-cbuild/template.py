pkgname = "base-cbuild"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
pkgdesc = "Core package set for cbuild containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# musl must be built first to provide shlibs for later packages during stage 0
depends = [
    "musl-devel", "elftoolchain", "llvm", "clang", "lld", "bsdutils", "awk",
    "apk-tools", "bsdutils-extra", "bmake", "bsdtar", "ncurses",
    "util-linux-cbuild", "tzdata", "fakeroot",
]

options = ["bootstrap", "brokenlinks"]

if self.stage > 1:
    depends += ["ccache", "ca-certificates"]
