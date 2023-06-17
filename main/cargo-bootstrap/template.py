pkgname = "cargo-bootstrap"
pkgver = "1.70.0"
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
            "9c0fb0230a81074572f0c7dbb0557d9e16baa078c73b250908d97854dcd84fb0"
        )
    case "ppc64le":
        sha256 = (
            "93c41a591be0615a2c804cb249f53eb9b83b0cfde4958fb4291ec1a2cb15a0b4"
        )
    case "ppc64":
        sha256 = (
            "d193ed37ea48e0b3b668325fd892159a99affcb969e0cbd6a9ec0ef5f0068504"
        )
    case "riscv64":
        sha256 = (
            "d55af3d6622acf92407eb6c5a5af0db8833d633f8b08d5bbe6924aeabb3a5098"
        )
    case "x86_64":
        sha256 = (
            "f01449d4f21a718a63a2c47eda938a5fd191d7686d04c5d37f95e7df5b921d30"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
