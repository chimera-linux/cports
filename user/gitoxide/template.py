pkgname = "gitoxide"
pkgver = "0.42.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gix-features/zlib-stock,gitoxide-core-blocking-client,http-client-curl",
]
make_install_args = [*make_build_args]
make_check_args = [*make_install_args]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "curl-devel",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Rust implementation of Git"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4f7febd1bc45d96afc643142d26753ccb7fde7e69f68ca201f04953c1fc6ba7a"


def post_install(self):
    self.install_license("LICENSE-MIT")
