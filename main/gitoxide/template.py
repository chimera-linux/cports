pkgname = "gitoxide"
pkgver = "0.37.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gix-features/zlib-stock,gitoxide-core-blocking-client,http-client-curl",
]
make_install_args = [*make_build_args]
make_check_args = [*make_install_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "curl-devel",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Rust implementation of Git"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1bdc30bafdd3605d6e278aa5562f772a9732bb07ced9321ea31893b28f950c0a"


def post_install(self):
    self.install_license("LICENSE-MIT")
