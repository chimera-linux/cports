pkgname = "yazi"
pkgver = "0.4.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "Terminal file manager"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://yazi-rs.github.io"
source = f"https://github.com/sxyazi/yazi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "88995c90954d140f455cf9ca4f87f9ca36390717377be86b0672456e1eb5f65f"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    for binary in ["yazi", "ya"]:
        self.install_bin(f"./target/{self.profile().triplet}/release/{binary}")

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="yazi.png")
    self.install_file("assets/yazi.desktop", "usr/share/applications")
    self.install_license("LICENSE")
