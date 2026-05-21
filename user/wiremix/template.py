pkgname = "wiremix"
pkgver = "0.10.0"
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
sha256 = "dfb165ff664b804099c5592fd26d2b03d78e67069522bc5d3d8ef75a19505adf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_file("wiremix.desktop", "usr/share/applications")
    self.install_file("wiremix.toml", "usr/share/examples/wiremix")
