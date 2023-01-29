pkgname = "cargo-bootstrap"
pkgver = "1.67.0"
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
        sha256 = "715f44918bacd9246e551669a0bcb8f15740a0c2fbe801e63a3bf928760441e0"
    case "ppc64le":
        sha256 = "66fd87b8b6c5addb3738275645aa623f262b9259910a3536be484fe6f1fb4b60"
    case "riscv64":
        sha256 = "22ed6386d7347976cfd451732f909e91094d1912ce9350bd82efc3392e7772bf"
    case "x86_64":
        sha256 = "00604ce0c4b1f3b7ca15324d50a4cd809511a9fed1f5e44cff655c56aa221b3e"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
