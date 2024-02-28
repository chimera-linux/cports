pkgname = "cargo-bootstrap"
pkgver = "1.75.0"
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
            "9deafc34b7086a020b6d9d695557485b2ac38cf8b8d6cee8373290cd003a0a55"
        )
    case "ppc64le":
        sha256 = (
            "e27b9bb68f3e9449a2124886756d4b7c204846e28b82066f74ccc5921a55fff5"
        )
    case "ppc64":
        sha256 = (
            "7435482f1611009f81b8a216633ab0ec6a11941f0b5832db6a1ddb3abdf944e2"
        )
    case "riscv64":
        sha256 = (
            "4436dfc02b65b5e1fa9779e4856fe458ed45a4c777201ecf48449d79a09d7660"
        )
    case "x86_64":
        sha256 = (
            "c94ddf703534a4df315402db2ccacccfeeb7c4bf99e678dcd84666bc84565e7c"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
