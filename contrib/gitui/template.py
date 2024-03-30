pkgname = "gitui"
pkgver = "0.26.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=ghemoji,regex-onig,vendor-openssl",
]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = ["cargo-auditable", "pkgconf"]
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
sha256 = "b1b0a6c692771a4e37f7ff33490365f8f330660a4110adf650b2483d99379c1d"
env = {"GITUI_RELEASE": "1"}


def pre_prepare(self):
    self.rm(".cargo/config")


def post_install(self):
    self.install_license("LICENSE.md")
