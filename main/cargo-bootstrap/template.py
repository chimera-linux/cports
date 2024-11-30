pkgname = "cargo-bootstrap"
pkgver = "1.82.0"
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
            "08df611e582eafc2da662dd37da2aebd78d1148dcef57d240fe3c47742277614"
        )
    case "ppc64le":
        sha256 = (
            "a00378c7b88b722c8984929aa03fb2e8ae6e21270d28af05c767e9da551874a9"
        )
    case "ppc64":
        sha256 = (
            "76368bb3321aee21d4cd38692cc834badb516b017ba8142ee6fce6edd5f7893c"
        )
    case "riscv64":
        sha256 = (
            "2c7a5dfc86c881b10e14ada1502bd04b35c6a791d35fdcef4608c6e87a4d924b"
        )
    case "x86_64":
        sha256 = (
            "28bb0371cd54263a3f39fa4ebf4c0229c6afaa6d9e8811957be643b3c5d7f8c1"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
