pkgname = "cargo-deny"
pkgver = "0.18.2"
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
sha256 = "bb47741fada886c166e2a697a87fe93fca38ec083db489d404c73bcb0b9d7445"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
