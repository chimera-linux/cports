pkgname = "cargo-bootstrap"
pkgver = "1.73.0"
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
            "bb5a79e594f6f52ba510a624114f31cfc36e5fe69d56e32cf76913c6ef9510d5"
        )
    case "ppc64le":
        sha256 = (
            "f6ed1b44ed617005ba04efee0a671b993ec30956e5ae81a534f31466db780f87"
        )
    case "ppc64":
        sha256 = (
            "438175b430d615eda1dcfec860088c530589700c9109aad82c5046cd253f10aa"
        )
    case "riscv64":
        sha256 = (
            "74268aef96b6b4ccd358e2b3fb1dd01b3438381086bb1c98a400d04f85a746c0"
        )
    case "x86_64":
        sha256 = (
            "b5c1a35b09b4c2a5839d2fb3053fa6c016df0d61156663ebd98f36d1cb3607af"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
