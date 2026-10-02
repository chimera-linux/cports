pkgname = "cargo-bootstrap"
pkgver = "1.98.0"
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
            "5725e4c3738d88750567a3d60288367d659f25d1f443698905675f51472747c8"
        )
    case "loongarch64":
        sha256 = (
            "0de4c7ec4350240f1207dff51759e5ac5849e181e70d92e82baa632f99459b07"
        )
    case "ppc64le":
        sha256 = (
            "da530d915d4cb718002d86e5fdff0a648132bfec2a1bac36d97c112256d87f87"
        )
    case "riscv64":
        sha256 = (
            "f8bb16ab4c1436b3043ef2069131cef892c2e10eddc996957e08a56834f4553e"
        )
    case "x86_64":
        sha256 = (
            "6bbba14e8d077c661b849ecf99dace5810538aa2c22b3cb382c1123510c4aa4b"
        )
    case _:
        broken = f"not yet built for {self.profile.arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
