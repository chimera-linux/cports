pkgname = "cargo-deny"
pkgver = "0.19.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
depends = ["ca-certificates"]
pkgdesc = "Cargo plugin for linting dependencies"
license = "MIT OR Apache-2.0"
url = "https://github.com/EmbarkStudios/cargo-deny"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f69e6472a02c6059c2813170d9767ff7305862c82d7b6a09dea8cb1e67648b73"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
