pkgname = "cargo-bootstrap"
pkgver = "1.97.1"
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
            "e475fcc160ba3c3ec000f4db2c4b9bc1dd48af176399cef611ab06635a98e4a2"
        )
    case "loongarch64":
        sha256 = (
            "6318729f476eca0aed8314a1275c21f47d7c784f59854cf52abc90da10b1555a"
        )
    case "ppc64le":
        sha256 = (
            "a62fb4586fb2f0222c645f39e5e8aa60833e09cdaf6765d00dc28807c54de813"
        )
    case "riscv64":
        sha256 = (
            "4d9c3f33f538b5433616e0f267ec156960eb7e192cc668ee02581ab2ba544f3f"
        )
    case "x86_64":
        sha256 = (
            "34f00f0721f90755db57881284cefa9bfc53945a10fdb2199e2bafa05a0b195f"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
