pkgname = "gitoxide"
pkgver = "0.35.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gix-features/zlib-stock,gitoxide-core-blocking-client,http-client-curl",
]
make_install_args = list(make_build_args)
make_check_args = list(make_install_args)
hostmakedepends = ["cargo", "pkgconf"]
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
sha256 = "4f074b30830ff37da8ae9de11b0441addea9f1552f0fcac1fa6fb56435d5bbea"


def post_install(self):
    self.install_license("LICENSE-MIT")
