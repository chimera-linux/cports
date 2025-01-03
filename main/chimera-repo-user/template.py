pkgname = "chimera-repo-user"
pkgver = "0.2"
pkgrel = 0
archs = ["aarch64", "ppc", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "meta"
depends = ["chimera-repo-main"]
pkgdesc = "Chimera user repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        self.files_path / "01-repo-user.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "01-repo-user-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-user-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["etc/apk/repositories.d/*-debug.list"]
