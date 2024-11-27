pkgname = "systeroid"
pkgver = "0.4.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI and helper tool for sysctl values"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 OR MIT"
url = "https://systeroid.cli.rs"
source = (
    f"https://github.com/orhun/systeroid/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b638d1167227a30cf793847a08fee42a5810bfb6a493ea0289e29c8260ef916c"
# needs kernel docs to exist
options = ["!check"]


def install(self):
    self.install_license("LICENSE-MIT")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid-tui")
    self.install_man("man8/systeroid.8")
    self.install_man("man8/systeroid-tui.8")
