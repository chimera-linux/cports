pkgname = "chimera-repo-contrib"
pkgver = "0.6.9"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "meta"
build_style = "meta"
depends = ["chimera-repo-main"]
pkgdesc = "Transitional package for former contrib repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("chimera-repo-contrib-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return []
