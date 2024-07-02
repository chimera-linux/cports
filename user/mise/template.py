pkgname = "mise"
pkgver = "2024.12.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Dev tools, env vars, task runner"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0763599841970d9a60630fbd97301d7a06d9ce5c61d9da657fda432f2204cfae"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
