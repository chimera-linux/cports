pkgname = "chimera-repo-main"
pkgver = "0.2"
pkgrel = 0
archs = ["aarch64", "ppc", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "meta"
depends = ["apk-tools", "!base-cbuild"]
pkgdesc = "Chimera base repository"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        *self.find(
            self.files_path, f"{self.profile().arch}@chimera-linux.org-*.pub"
        ),
        "etc/apk/keys",
    )
    self.install_file(
        self.files_path / "q66@chimera-linux.org-61a1913b.rsa.pub",
        "etc/apk/keys",
    )
    self.install_file(
        self.files_path / "00-repo-main.list", "etc/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "00-repo-main-debug.list", "etc/apk/repositories.d"
    )


@subpackage("chimera-repo-main-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["etc/apk/repositories.d/*-debug.list"]
