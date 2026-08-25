pkgname = "gitoxide"
pkgver = "0.58.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gitoxide-core-blocking-client,http-client-curl,sha1",
]
make_install_args = [*make_build_args]
make_check_args = [*make_install_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "curl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Rust implementation of Git"
license = "Apache-2.0 OR MIT"
url = "https://github.com/Byron/gitoxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "af8210e01903e0995aa5899d8c8cd3f4f2b115ec38a924fa7bf3c7d8ba949077"


def post_install(self):
    self.install_license("LICENSE-MIT")
