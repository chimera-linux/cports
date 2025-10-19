pkgname = "systeroid"
pkgver = "0.4.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI and helper tool for sysctl values"
license = "Apache-2.0 OR MIT"
url = "https://systeroid.cli.rs"
source = (
    f"https://github.com/orhun/systeroid/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "756b341dc86553ce8df583d55e6d01517bf52721a556713a4fb6056c0f823f3b"
# needs kernel docs to exist
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"


def install(self):
    self.install_license("LICENSE-MIT")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid-tui")
    self.install_man("man8/systeroid.8")
    self.install_man("man8/systeroid-tui.8")
