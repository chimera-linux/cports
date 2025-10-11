pkgname = "gping"
pkgver = "1.20.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=test_integration",
    "--skip=linux::tests::test_linux_detection",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libgit2-devel"]
pkgdesc = "TUI ping tool with a graph"
license = "MIT"
url = "https://github.com/orf/gping"
source = f"{url}/archive/refs/tags/gping-v{pkgver}.tar.gz"
sha256 = "0df965111429d5fcef832a4ff23b452a1ec8f683d51ed31ce9b10902c0a18a9c"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gping")
    self.install_man("gping.1")
    self.install_license("LICENSE")
