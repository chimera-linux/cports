pkgname = "cargo-bootstrap"
pkgver = "1.89.0"
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
            "d5ba2bed7a314e878de03e19a4dee8f428e0f3d0e5646c049113a27007dbf0d7"
        )
    case "loongarch64":
        sha256 = (
            "b0984c39781924b6abf6afba0c5a425f0c535a20103d946a7372252bfe5ecb68"
        )
    case "ppc64le":
        sha256 = (
            "b931db02cd25707515de0f7e4d97dea1b7a9006f6b30e3d4045c0bea05d978e1"
        )
    case "ppc64":
        sha256 = (
            "eeef1c2c6ef66388a550d5bf16a8c42d70a91dbb760a82c0e1f958a46d4991a8"
        )
    case "ppc":
        sha256 = (
            "d4f293c237dedebc1766b0db9e391ec30a5c5dbc598c519ed10bcf6b698dd1d3"
        )
    case "riscv64":
        sha256 = (
            "5b845ff411fc321f9f93708ecf9fe7274f77fdb3047f76a0e7d71d54ed8435f3"
        )
    case "x86_64":
        sha256 = (
            "13c7cab92b56237198a584461474ffeb74eedf4f80dc430fd9dbd2766c725c11"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
