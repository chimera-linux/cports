pkgname = "wiremix"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "pipewire-devel",
    "rust-std",
]
pkgdesc = "TUI audio mixer for PipeWire"
license = "MIT OR Apache-2.0"
url = "https://github.com/tsowell/wiremix"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "62a7cace79c9af537e0917a6d4e5da66b2efe2b4abc5f08c0fbaed727acc8c9f"

if self.profile().wordsize == 32:
    broken = "nix shenanigans"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_file("wiremix.desktop", "usr/share/applications")
    self.install_file("wiremix.toml", "usr/share/examples/wiremix")
