pkgname = "gitoxide"
pkgver = "0.46.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=max-control,gitoxide-core-blocking-client,http-client-curl",
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
sha256 = "68a60cae90e0882cb3e1e699bc1c7e64902b632cc30209f60444c8ca8b2d820e"


def post_install(self):
    self.install_license("LICENSE-MIT")
