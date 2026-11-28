pkgname = "cargo-bootstrap"
pkgver = "1.99.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib-ng-compat"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile.triplet}.tar.xz"
options = ["!strip"]

match self.profile.arch:
    case "aarch64":
        sha256 = (
            "7df294a80137456b7de504cc71afba5de4f11ac9a0b5c7ea36f0508b426b05a7"
        )
    case "loongarch64":
        sha256 = (
            "2a8f50a34106ae9877e982cbe771260b9fa16ddc3ad11a8bba9e3d8168184c59"
        )
    case "ppc64le":
        sha256 = (
            "0dac549b0df8f94aaae07adcdbd18be337861fddf9a4acc845a0d55fbc4d228c"
        )
    case "riscv64":
        sha256 = (
            "b5afd3a91a64a7b5cc4e7d9eea3d7c9fdd6169afc9730d150a6ba70562997cc0"
        )
    case "x86_64":
        sha256 = (
            "f55485f56b37158641494805ac14134003a986a444cc14b3dc6c0dada28be36b"
        )
    case _:
        broken = f"not yet built for {self.profile.arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
