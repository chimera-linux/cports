pkgname = "cargo-bootstrap"
pkgver = "1.83.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib-ng-compat"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "cef5ea039eba1318042075cb8fc38ca776bfde4e43fad78099d6baf2eed2fee2"
        )
    case "ppc64le":
        sha256 = (
            "e4fd97cf7fddd9b4f759a50483ffdb69a4b5691bd8a0e2cb082d5463e386b23e"
        )
    case "ppc64":
        sha256 = (
            "bd68d0b26b443e904d2c59fb035706a9999d5043570fc59107b0b9f14e286d8e"
        )
    case "ppc":
        sha256 = (
            "a53f6159bd2ef191a1da0bbb37e311964268304ce73bc860a95a3015160b5b8c"
        )
    case "riscv64":
        sha256 = (
            "8f28fd11da2737545d3ccb7794e74cbc9ce8024f8dd6dd721957e9a39b083b3a"
        )
    case "x86_64":
        sha256 = (
            "8f0c3ac6719db4ed27c7c752c6e9dc0cbf48fe15d965129e3939de2d42a85258"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
