pkgname = "cargo-bootstrap"
pkgver = "1.86.0"
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
            "b08f8bb99985a0625469506c25e0a9d8923ee745ee8008aad18f5bce984e9267"
        )
    case "loongarch64":
        sha256 = (
            "966b20005fe1b5d482040439e5fb592505fac86aed034b9649fd14b9bd2664a7"
        )
    case "ppc64le":
        sha256 = (
            "929585a492dc6cda76434599a0a417cfdc830d6a9d61c9ab69c2c7e9bfdfe86f"
        )
    case "ppc64":
        sha256 = (
            "b55a2582507bcb882800d1855f4fd8630d897838fe68a398030be9cde788e608"
        )
    case "ppc":
        sha256 = (
            "21cba1a030c58e3855b5ec7d1326266254f2b46e8f5ddf9a4a9bddf63bd874c2"
        )
    case "riscv64":
        sha256 = (
            "e25ce707fcfe0f0e238954d1b57ab6035714cd21404e27b7308abcc9a77da24d"
        )
    case "x86_64":
        sha256 = (
            "c7710dcee60e273f7a738a0bce3f2d4f67d7056af35b2929b6ca6090853c9ab0"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
