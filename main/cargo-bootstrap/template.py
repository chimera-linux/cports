pkgname = "cargo-bootstrap"
pkgver = "1.92.0"
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
            "75a37e9689b5ff8fa53d397e23677f78179b57858383d7048c87cba5712c90dd"
        )
    case "loongarch64":
        sha256 = (
            "deaa28b3cf0b21994e6240e781c39f55f762fd097534e563ae416a69c061c1ff"
        )
    case "ppc64le":
        sha256 = (
            "3d1e74a725d8e71ae2d303313b4a3a92f4b216234046b792b380db158567bd59"
        )
    case "ppc64":
        sha256 = (
            "befa791b8f849bf7f8c6fecaa6ddd2e06cf3a5149e51c378a6c46b7fa5e02b2a"
        )
    case "ppc":
        sha256 = (
            "424bf4333eb6d0eb10e7c7b4068de521e2115a5f04ba077e33ea9e1177d7a3e1"
        )
    case "riscv64":
        sha256 = (
            "476ac9b197d1483480b8cb05e18175d7d83f02eaa9007fead485999f0dd01177"
        )
    case "x86_64":
        sha256 = (
            "6397788657cfafc224252a31f50e39818b0e31d042cd459ef29a8764b28b7627"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
