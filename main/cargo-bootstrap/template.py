pkgname = "cargo-bootstrap"
pkgver = "1.88.0"
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
            "e41899c8fb2e68add95c0a20690d50ff2326cf285163496319004fa195558093"
        )
    case "loongarch64":
        sha256 = (
            "3e912bfefa106c584dc379cb54cda57fcc8fdfd3fb65fc18d66b36812426f774"
        )
    case "ppc64le":
        sha256 = (
            "20df9df129e233f472e43f149afb0dfc06a2be5e387322c266b68a9faf218b84"
        )
    case "ppc64":
        sha256 = (
            "2ece26cb0ac6d9aa6ef3cba41cbd158c9b9b29a363a1e2e3672f8852ea8a7182"
        )
    case "ppc":
        sha256 = (
            "fa8a22dc463e9770b976ebcb3ef5353cdf7f1290ac5b961b4027285a24085a09"
        )
    case "riscv64":
        sha256 = (
            "3a36a39661a80c35493251ceee35bccfe9c17628bcf9a613ebb235f76360fa43"
        )
    case "x86_64":
        sha256 = (
            "50be691ab70dcccbf3ea620310b970652aba0c7b920110b285dbe9ca119ea970"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
