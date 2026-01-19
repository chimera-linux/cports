pkgname = "wiremix"
pkgver = "0.8.0"
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
pkgdesc = "Simple TUI audio mixer for PipeWire"
license = "MIT OR Apache-2.0"
url = "https://github.com/tsowell/wiremix"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "db357d21c76809d674024f1094c2ac6ddd2d6866d4b8ae53cbb0620599006e31"
hardening = ["vis", "cfi"]


def post_patch(self):
    self.do("cargo", "rm", "--build", "vergen-git2")


def pre_configure(self):
    self.env["VERGEN_GIT_DESCRIBE"] = f"v{self.pkgver}"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
    self.install_file("wiremix.desktop", "usr/share/applications")
    self.install_file("wiremix.toml", "usr/share/examples/wiremix")
