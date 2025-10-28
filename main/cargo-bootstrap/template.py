pkgname = "cargo-bootstrap"
pkgver = "1.90.0"
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
            "b5a45ea660c8be12eb54089f97f724330dc832c642e9de170bb5579264013758"
        )
    case "loongarch64":
        sha256 = (
            "895e5bcc1e65d63709453282fc46b74674e68f35c23d260480eac664dfaf5d8b"
        )
    case "ppc64le":
        sha256 = (
            "0fe49da9cfb6eb6f88c84daef6cdfa49b9e18f8b113888602737dd538c0021da"
        )
    case "ppc64":
        sha256 = (
            "e007df2483af6758fb926e2970b302c1d80eb52f38ca5d410a36232f8ef6dc81"
        )
    case "ppc":
        sha256 = (
            "d9c8fd92fc83ae551d1ff30bcebc75fa4cde31f595c3b7c36248c8747f27d566"
        )
    case "riscv64":
        sha256 = (
            "ac8e71f51d9fb9461f9a8586253dd59d0ef2bbf18e6523e4f0f5e2dbb2b69ec6"
        )
    case "x86_64":
        sha256 = (
            "2355ed50ee9369796806634ad2af614657d5af81e0f2c1c2b090eebfe2aa8fcf"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
