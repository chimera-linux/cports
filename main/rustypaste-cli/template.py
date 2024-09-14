pkgname = "rustypaste-cli"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=use-native-certs",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI client for rustypaste"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/orhun/rustypaste-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5defaf6357e2ab8dc7b0e3f3e9e2012b79590b0af6cf16dd65ef0eabfb7c73a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rpaste")
    self.install_license("LICENSE")
    self.install_man("man/rpaste.1")
