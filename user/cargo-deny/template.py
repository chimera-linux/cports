pkgname = "cargo-deny"
pkgver = "0.18.5"
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
sha256 = "d04cb7b0b9f75c483dc37d72970a8c759674d1a7b882aaae2c56a60fe18361ab"
# TODO
options = ["!check"]

if self.profile().arch == "loongarch64":
    broken = "busted rustix"


def post_install(self):
    self.install_license("LICENSE-MIT")
