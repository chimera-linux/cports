pkgname = "chimera-repo-user"
pkgver = "0.3"
pkgrel = 0
archs = [
    "aarch64",
    "loongarch64",
    "ppc",
    "ppc64",
    "ppc64le",
    "riscv64",
    "x86_64",
]
build_style = "meta"
depends = ["chimera-repo-main"]
pkgdesc = "Chimera user repository"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        self.files_path / "11-repo-user.list", "usr/lib/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "12-repo-user-debug.list",
        "usr/lib/apk/repositories.d",
    )


@subpackage("chimera-repo-user-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["usr/lib/apk/repositories.d/*-debug.list"]
