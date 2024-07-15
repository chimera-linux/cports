pkgname = "cargo-deny"
pkgver = "0.14.24"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Cargo plugin for linting dependencies"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/EmbarkStudios/cargo-deny"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e5cde78e62af26676c75875abe86119437b8e20537d7062111c423d05a1fc3d0"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
