pkgname = "gitoxide"
pkgver = "0.41.0"
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
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6c90676da83e4aa202ac08c6ce849d31031310953569d5fee7529437778b6273"


def post_install(self):
    self.install_license("LICENSE-MIT")
