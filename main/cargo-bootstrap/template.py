pkgname = "cargo-bootstrap"
pkgver = "1.84.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib-ng-compat"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "dd6501b9662f419c34b371609682ae48e9522af255c346baecf9d95011f85302"
        )
    case "ppc64le":
        sha256 = (
            "c19351f01361b8173c97d89d8f5601889f2344aff7783eed085f891f96ef9720"
        )
    case "ppc64":
        sha256 = (
            "7e0d8f14f75cd2f3c63fcb66931e29309198fcade373109048e277811a0d2fb0"
        )
    case "ppc":
        sha256 = (
            "a055556bee0a1429fa56b49a41c5c4b61d57f311b4ec9d0f37ffbbd87ce6aef6"
        )
    case "riscv64":
        sha256 = (
            "70745411e15fef16003aa1177d3f30f8c78cbf062a9fc5ba446003eec53a30c8"
        )
    case "x86_64":
        sha256 = (
            "0156a80877a1f468eac447abdea3eb6ed03048c255d919bfe72104209a50fb5f"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
