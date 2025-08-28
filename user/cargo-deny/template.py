pkgname = "cargo-deny"
pkgver = "0.18.4"
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
sha256 = "cd093a71d383988252428ebc08ee83f9db204e95074138264f9c8bd5fa06369a"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
