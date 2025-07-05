pkgname = "sway-overfocus"
pkgver = "0.2.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Better focus navigation for sway and i3"
license = "MIT"
url = "https://github.com/korreman/sway-overfocus"
source = f"https://github.com/korreman/sway-overfocus/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fc5f8103e740a21bb34083bb5cd06291c0d059cea502f693320d98f31817647f"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sway-overfocus")
    self.install_license("LICENSE")
