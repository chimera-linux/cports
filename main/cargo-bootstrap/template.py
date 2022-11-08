pkgname = "cargo-bootstrap"
pkgver = "1.65.0"
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
        sha256 = "ad05420c63d98de166c96803a4374b3bc5f600dcd498615ac5e52a92e8a819c6"
    case "ppc64le":
        sha256 = "b989dd64572ade799bb658a1588f77d729d673aa9ca2585a6f4183ad47ce779f"
    case "riscv64":
        sha256 = "0787747efa32c00565ed238af468a232900086075b6d2b50f76e856b2081ef3d"
    case "x86_64":
        sha256 = "bb4de8a2781bb9aeef7a6259b14e7fe887949e913a4e536fcd365164ceddd933"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
