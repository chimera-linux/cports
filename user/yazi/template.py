pkgname = "yazi"
pkgver = "0.3.3"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "Terminal file manager"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "MIT"
url = "https://yazi-rs.github.io"
source = f"https://github.com/sxyazi/yazi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fe2a458808334fe20eff1ab0145c78d684d8736c9715e4c51bce54038607dc4e"


def install(self):
    for binary in ["yazi", "ya"]:
        self.install_bin(f"./target/{self.profile().triplet}/release/{binary}")

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="yazi.png")
    self.install_file("assets/yazi.desktop", "usr/share/applications")
    self.install_license("LICENSE")
