pkgname = "wiremix"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
    "pipewire-devel",
    "pkgconf",
    "clang",
    "libgit2-devel",
]
pkgdesc = "TUI audio mixer for PipeWire"
license = "MIT OR Apache-2.0"
url = "https://github.com/tsowell/wiremix"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "129bb85eca0e59dcc0e7e5306a3667d2ad4772baff346ec9fd4410fde796e5b4"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
