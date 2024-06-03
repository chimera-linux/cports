pkgname = "gitui"
pkgver = "0.26.3"
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
sha256 = "8075e180f3b01ff0c290b690488a7628c44b4de12346e04a77d823914a48918b"
env = {"GITUI_RELEASE": "1"}


def post_install(self):
    self.install_license("LICENSE.md")
