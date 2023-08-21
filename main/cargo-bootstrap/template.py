pkgname = "cargo-bootstrap"
pkgver = "1.71.0"
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
        sha256 = (
            "188cd7c22020b142fb6e909574ac44b5820d677a079847803a1a1eacfba9d012"
        )
    case "ppc64le":
        sha256 = (
            "286cdbe2ed94884a598c6f4617dd3ca3c389e20e3095efb3ceb8137e53697087"
        )
    case "ppc64":
        sha256 = (
            "77f10aceafb393d283735e0fb9f4fdbaee185735bee80045c1aa65c784aba85e"
        )
    case "riscv64":
        sha256 = (
            "ef112aeb3801ead2f3304e09358add9546c968d1688d59925a9e17e45b64a8fb"
        )
    case "x86_64":
        sha256 = (
            "07c52f3a235b5712e717243450e67a3777fbc1f3f40560220977245cb1a9b727"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
