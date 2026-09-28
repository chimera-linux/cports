pkgname = "cxxbridge"
pkgver = "1.0.150"
pkgrel = 0
build_wrksrc = "gen/cmd"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
depends = ["rust-std"]
pkgdesc = "C++ code generator for `cxx` in non-Cargo builds"
license = "MIT OR Apache-2.0"
url = "https://github.com/dtolnay/cxx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4a8e771cb8dcc6588c25270ad4e6b2668f238434d42ae8bc8ee6c6da0ac165e7"


def post_install(self):
    self.install_license("LICENSE-MIT")
