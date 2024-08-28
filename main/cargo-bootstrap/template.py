pkgname = "cargo-bootstrap"
pkgver = "1.79.0"
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
            "aa9d877909616144327040ed088ac03196071db6d343eef4e73f4b0d9c5d3844"
        )
    case "ppc64le":
        sha256 = (
            "9f8c8d48a3e8855ce18e7fd05bf2fd8d7def921cf45625581cb1ca661154bea6"
        )
    case "ppc64":
        sha256 = (
            "f36c244e32230233f1fbfb53365b13699d7ee57b57c1096b372a28b3768ceb40"
        )
    case "riscv64":
        sha256 = (
            "2ea29323569f5a455db10cfbde9962acddcd4e3fdf4d1ced9cc11b25bd63b61b"
        )
    case "x86_64":
        sha256 = (
            "f864321aab8353658932c53a672528f2d5b44ded39acea7f1ee82a07b92ebe3b"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
