pkgname = "chimera-repo-contrib"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "meta"
depends = ["chimera-repo-main"]
pkgdesc = "Chimera contrib repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        self.files_path / "01-repo-contrib.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "01-repo-contrib-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-contrib-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["etc/apk/repositories.d/*-debug.list"]
