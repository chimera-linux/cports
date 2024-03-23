pkgname = "gitui"
pkgver = "0.25.2"
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
sha256 = "5a67d526e22533952a747cb34eb2430a1340dd3139f60a785f579bba4a6aa5ed"


def pre_prepare(self):
    self.rm(".cargo/config")


def post_install(self):
    self.install_license("LICENSE.md")
