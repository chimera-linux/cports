pkgname = "cargo-bootstrap"
pkgver = "1.81.0"
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
            "d8d9be963a5d7d34ba5b73deeb946b9fa6aa3f404926bc6540e5415c37f2a54e"
        )
    case "ppc64le":
        sha256 = (
            "4d849d5c2c4f3a0920b69835d02fb37a3ff23af4161bb42d5256d6e6db9347ec"
        )
    case "ppc64":
        sha256 = (
            "1f4d7b8b00e5682c8064ec312cfb6990e26133e7d2323d70a6e0a8872a138c2a"
        )
    case "riscv64":
        sha256 = (
            "70517e96d2ec7607019c451838253d49b4d9853d3b51208de6158f27b94b5341"
        )
    case "x86_64":
        sha256 = (
            "df47c2fabad1cd26b83910a35eeaddae21997af310ba87b2fc2bd580fb695ce0"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
