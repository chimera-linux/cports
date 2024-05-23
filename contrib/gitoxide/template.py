pkgname = "gitoxide"
pkgver = "0.36.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gix-features/zlib-stock,gitoxide-core-blocking-client,http-client-curl",
]
make_install_args = list(make_build_args)
make_check_args = list(make_install_args)
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libcurl-devel",
    "rust-std",
    "sqlite-devel",
    "zlib-devel",
]
pkgdesc = "Rust implementation of Git"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "36142c7388c68732a953fcfd9dcd609241b1d9a5d2fdb2e796e987b6b6872fa7"


def post_install(self):
    self.install_license("LICENSE-MIT")
