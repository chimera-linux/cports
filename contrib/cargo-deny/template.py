pkgname = "cargo-deny"
pkgver = "0.14.24"
pkgrel = 1
build_style = "cargo"
make_build_args = ["--no-default-features", "--features=native-certs"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
depends = ["ca-certificates"]
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
