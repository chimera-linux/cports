pkgname = "cargo-bootstrap"
pkgver = "0.58.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# overlapping files
depends = ["virtual:rust-bootstrap-virtual", "!cargo"]
depends_providers = {
    "virtual:rust-bootstrap-virtual": "rust-bootstrap"
}
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://ftp.octaforge.org/q66/random/rust-chimera/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "3957fb1298df0d1bf8bb0e9fd6e315167747f4c79838252845028898b81c15fc"
    case "ppc64le":
        sha256 = "927f494ae2b2bac9ebb17f15d3714287169be9d1bd9b4143f5669764d4cd10ac"
    case "x86_64":
        sha256 = "b1ea49fb1ec67057686e0959df55de1c16bddfb0b9340271d45ca7845017198b"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
