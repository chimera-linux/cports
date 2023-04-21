pkgname = "cargo-bootstrap"
pkgver = "1.69.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["zlib"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "1cb83f6bbb424310a35a10e7934c49f2395750f0a72bd169e3e1531e68db0c31"
    case "ppc64le":
        sha256 = "ece21c1f4c5629ce9601772da5f192b9689811fb215d7e7ffa7d709700de7e24"
    case "riscv64":
        sha256 = "39737f9c615b5185f39f376ad2cb634189e0ea7e0527d391eeda8ec82afd2a05"
    case "x86_64":
        sha256 = "7f315879a6033cbe86919fba3f2dd4bcbdb9a078f725a473619122681ed5bc65"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
