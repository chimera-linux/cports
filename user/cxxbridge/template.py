pkgname = "cxxbridge"
pkgver = "1.0.136"
pkgrel = 0
build_wrksrc = "gen/cmd"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
depends = ["rust-std"]
pkgdesc = "C++ code generator for `cxx` in non-Cargo builds"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT OR Apache-2.0"
url = "https://github.com/dtolnay/cxx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a77e43f1e4f5bb6aba2e9a77ac928e63799d237cde6fe1aa2c26d3cc57c8ae74"


def post_install(self):
    self.install_license("LICENSE-MIT")
