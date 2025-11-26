pkgname = "cargo-deny"
pkgver = "0.18.6"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features=native-certs"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
depends = ["ca-certificates"]
pkgdesc = "Cargo plugin for linting dependencies"
license = "MIT OR Apache-2.0"
url = "https://github.com/EmbarkStudios/cargo-deny"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9f4227c5eb94011cc32601e8f2acbf6651ab7ee632cda2e5e05e242207a07d73"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
