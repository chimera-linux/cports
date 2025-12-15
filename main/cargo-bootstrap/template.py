pkgname = "cargo-bootstrap"
pkgver = "1.91.0"
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
            "578bedb56c465a08ccb710753738e1e441c9a24924aff7df3d7f00d325948b87"
        )
    case "loongarch64":
        sha256 = (
            "3bb189a53273304660481a9fc3a5cf1430408857d52ddcc3fce96cc2cfc8a555"
        )
    case "ppc64le":
        sha256 = (
            "cb848236882e54fcf2eb52d3bf8607266b8efaf6c3125025f0aff5f4ef330268"
        )
    case "ppc64":
        sha256 = (
            "eb3d1e44549a21d992e2bf95cdce6ae85a7cec9058d03e558c6dc9258ddba136"
        )
    case "ppc":
        sha256 = (
            "bc07befb5aecd6b4e4213b9e53c4e060142b62fec6d632984e2fdfa6f28adf83"
        )
    case "riscv64":
        sha256 = (
            "edee1ed229c880827f3bd80cf57a875bd53df330ea9f7f9e6fa9465cc8784bbf"
        )
    case "x86_64":
        sha256 = (
            "a5371229435769312a3b84b9bacfc168feb34f8309071894ecc2b335f9af659a"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
