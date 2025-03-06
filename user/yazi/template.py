pkgname = "yazi"
pkgver = "25.3.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "Terminal file manager"
license = "MIT"
url = "https://yazi-rs.github.io"
source = f"https://github.com/sxyazi/yazi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bc1a7b6cd69310ea3369bec2a618e7a0f683f7d25f41a1abdcab82f6a1886bab"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    for binary in ["yazi", "ya"]:
        self.install_bin(f"./target/{self.profile().triplet}/release/{binary}")

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="yazi.png")
    self.install_file("assets/yazi.desktop", "usr/share/applications")
    self.install_license("LICENSE")
