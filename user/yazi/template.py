pkgname = "yazi"
pkgver = "26.5.6"
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
sha256 = "a18445df86a20068f7b17609d12d6f635de488958579ae7a2b143a244ba7e63f"
# FIXME lintpixmaps
options = ["!lintpixmaps"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    for binary in ["yazi", "ya"]:
        self.install_bin(f"./target/{self.profile().triplet}/release/{binary}")

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="yazi.png")
    self.install_file("assets/yazi.desktop", "usr/share/applications")
    self.install_license("LICENSE")
