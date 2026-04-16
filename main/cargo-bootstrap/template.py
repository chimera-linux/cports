pkgname = "cargo-bootstrap"
pkgver = "1.94.0"
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
            "f2694ba80bb62ec201d05a5a47a243e7238beede1453a1aee392a2239dd34247"
        )
    case "loongarch64":
        sha256 = (
            "cdf2bdbe64ee4d72890b00fd9edf09a3b795b5274e63aece2e1a593b7e76e7ef"
        )
    case "ppc64le":
        sha256 = (
            "b0d4f5c44162a25e01df36e5ad358edbe3a9131ac57b912356670810f2aeff19"
        )
    case "ppc64":
        sha256 = (
            "125a852ac36c0ca773114a3520fd9d9f931849d0c217e68aa3290d5d00c6f17d"
        )
    case "ppc":
        sha256 = (
            "8696c54994a98e062f5e9ea09a152a4646dac469993fec5dfc8717aeb2cce274"
        )
    case "riscv64":
        sha256 = (
            "200c3edf0bfa91aedfdf8d41cbe330cd54334d0f17a483bb972c0215da9cfd7e"
        )
    case "x86_64":
        sha256 = (
            "46f4531d3989dd3659f1db801beb7ebbdc898bc390b2c288530e329470dbedff"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
