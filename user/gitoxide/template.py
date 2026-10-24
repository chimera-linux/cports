pkgname = "gitoxide"
pkgver = "0.61.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=hashes,max-control,gitoxide-core-blocking-client,http-client-curl",
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
sha256 = "52eef94ef7a4714189fc3c77a0a345a4f61d2e3b5a4dc472ea11115a05c8da40"


def post_install(self):
    self.install_license("LICENSE-MIT")
