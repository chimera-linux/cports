pkgname = "wl-clip-persist"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cargo"

hostmakedepends = ["cargo-auditable"]
makedepends = [
    "dinit-chimera",
    "rust-std",
    "turnstile",
]

pkgdesc = "Keep Wayland clipboard contents after source programs close"
license = "MIT"
url = "https://github.com/Linus789/wl-clip-persist"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fdd2506e6556dda943a164d891fe498985838fdd0e94c54e595a8f1cd8c49b66"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/wl-clip-persist")
    self.install_service(self.files_path / "wl-clip-persist.user")
    self.install_license("LICENSE")
