pkgname = "gitoxide"
pkgver = "0.45.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gitoxide-core-blocking-client,http-client-curl",
]
make_install_args = [*make_build_args]
make_check_args = [*make_install_args]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "curl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Rust implementation of Git"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1914573c9efa69a3a8b8ef97483a7756a4d5ab433a93e43502fb18332f77b623"


def post_install(self):
    self.install_license("LICENSE-MIT")
