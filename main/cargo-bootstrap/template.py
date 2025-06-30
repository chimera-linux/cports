pkgname = "cargo-bootstrap"
pkgver = "1.87.0"
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
            "a40bc15d01134491bb4e86423b00efa34383ea0e4e16526483c46cd074168549"
        )
    case "loongarch64":
        sha256 = (
            "e85619d446aa98a991ba21e213102dcbd2158c81c24bf07918e0d02ef66cd50e"
        )
    case "ppc64le":
        sha256 = (
            "9acdbc49507267b2bc51df23f580471b866ebf03d225bacecba5e4708c96c426"
        )
    case "ppc64":
        sha256 = (
            "acaa82410e07c055d398fff4368d913d7311c1e1b020dc202321fbba308f8fa5"
        )
    case "ppc":
        sha256 = (
            "675804c5067cc9aa9e7052f147caeefa7e97980bcba020fc9cc6e9a1f8c1d5e8"
        )
    case "riscv64":
        sha256 = (
            "682e261788a6f65e3f464627f59c70ae0dd37c2573a29b4cc1cebeb0e80e3193"
        )
    case "x86_64":
        sha256 = (
            "4aaabe2b37e966b201bd449d488ea5e25a17b3f34190faec88d079c6392571a3"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
