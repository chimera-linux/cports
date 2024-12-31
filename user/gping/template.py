pkgname = "gping"
pkgver = "1.19.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=test_integration",
    "--skip=linux::tests::test_linux_detection",
]
hostmakedepends = ["cargo-auditable"]
pkgdesc = "TUI ping tool with a graph"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/orf/gping"
source = f"{url}/archive/refs/tags/gping-v{pkgver}.tar.gz"
sha256 = "a979c9a8c7a1a540bb48a1e90bb7ad294560bddc16ca977bc8475fb14f20155d"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gping")
    self.install_man("gping.1")
    self.install_license("LICENSE")
