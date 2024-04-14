pkgname = "cargo-bootstrap"
pkgver = "1.76.0"
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
            "dfc2861a1e85d28d37bed802fa3f3a93c006ba72e30c140010d3634488876062"
        )
    case "ppc64le":
        sha256 = (
            "d81ce315ae39c98ab945ae670f0a7a69c5b1af794b13aaa2c984f75e3c9979a8"
        )
    case "ppc64":
        sha256 = (
            "d56fe811c6f83d287f8668e65c7c430adac29f70eed1d64e97a63a5b4033f92c"
        )
    case "riscv64":
        sha256 = (
            "c25c749164f07c096075b9bdc3608efc4ff963301978c46cb7dfce5598adbce3"
        )
    case "x86_64":
        sha256 = (
            "f5f40b487c9028e439eb23b70e93dcd2f1014876010a8a26948a2b742c02f9bd"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
