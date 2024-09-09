pkgname = "cargo-bootstrap"
pkgver = "1.80.0"
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
            "704f5b459035aaf5c429310e30ae1ac6026374c49f2d04d9ac59a73aa9b14be5"
        )
    case "ppc64le":
        sha256 = (
            "4d89b33177f815cb82673ebe033f27585df3c7d41ddc8a87b1efc597f6a15581"
        )
    case "ppc64":
        sha256 = (
            "39d54973e2575e8a76f0784bf2b954f7fda67302156aa82aabd626bb57e23b04"
        )
    case "riscv64":
        sha256 = (
            "76f4af68a66c7f323b6416b46359d74c9a533ebbbe48814ea84adf94281c0c5a"
        )
    case "x86_64":
        sha256 = (
            "18edce00b995f3692bee21469c7d05f71255c8609e80df37768f6f3365fc847d"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
