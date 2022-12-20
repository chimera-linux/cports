pkgname = "cargo-bootstrap"
pkgver = "1.66.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["zlib"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "8f8df8d78ef71facd008909defeab723f5f2d0d1435979dd5922cab5bc3a9f0b"
    case "ppc64le":
        sha256 = "01a0fcc1fe9fc38e0cd02a88a8f9085f137ff6befb9467b2d3a778009782dc9a"
    case "riscv64":
        sha256 = "089baa1830b1c4767a25f56ffc08c4f4a582594214815c164b55b6828d64c31f"
    case "x86_64":
        sha256 = "f2858aea88185ec30e8b7197e9c0c1a61d1a4d53bd8b5543249ad484173da0ac"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
