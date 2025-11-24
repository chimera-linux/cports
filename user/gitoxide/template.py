pkgname = "gitoxide"
pkgver = "0.47.0"
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
sha256 = "fea998534bfb1e0b91aa6960444468440bafe442f9fa5e197bbe8e7226d230f5"


def post_install(self):
    self.install_license("LICENSE-MIT")
