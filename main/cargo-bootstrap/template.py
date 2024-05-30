pkgname = "cargo-bootstrap"
pkgver = "1.77.1"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib"]
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
            "71662cf3259cd1e82fcede66f34aa97392c5a48ec6ba0aa4beb25638dd84b975"
        )
    case "ppc64le":
        sha256 = (
            "aa23a6bd5a27a39e6800ca5005f79151202eef8f0273f3ef8c196f5d4ab36717"
        )
    case "ppc64":
        sha256 = (
            "64b7e9209a05ffc0046842fa71fee2242d92bd50d86001027306a595d7a5158a"
        )
    case "riscv64":
        sha256 = (
            "778adfb7065fb5fb7ce8de17844b3ccaf4d181363522cd60b8cb61b0139a9a18"
        )
    case "x86_64":
        sha256 = (
            "0a2602863723fda8ac70377ff3718032da6517cf1848b6cf1efff7bfc6e37e33"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
