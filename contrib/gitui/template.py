pkgname = "gitui"
pkgver = "0.25.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=ghemoji,regex-onig,vendor-openssl",
]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "openssl-devel",
    "oniguruma-devel",
    "rust-std",
]
pkgdesc = "Terminal ui for git"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/extrawurst/gitui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78d31ba66de1521477aef1642c798a385106ff4858f59e79775ba08a694d0ae4"


def post_install(self):
    self.install_license("LICENSE.md")
