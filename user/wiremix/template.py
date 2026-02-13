pkgname = "wiremix"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
make_build_env = {"VERGEN_GIT_DESCRIBE": pkgver}
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
sha256 = "9fd8979fa3bc260a80d170c30041ab2aeea26273439bac8ce928a9405ce1d0f5"
hardening = ["vis", "cfi"]


def post_patch(self):
    self.do("cargo", "rm", "--build", "vergen-git2")


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_file("wiremix.desktop", "usr/share/applications")
    self.install_file("wiremix.toml", "usr/share/examples/wiremix")
