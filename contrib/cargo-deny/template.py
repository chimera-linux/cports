pkgname = "cargo-deny"
pkgver = "0.16.1"
pkgrel = 0
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
sha256 = "8e09aef97b0c299eefd23f019ad615559887f4ae3d54bd6affdd33a503a04fcf"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
