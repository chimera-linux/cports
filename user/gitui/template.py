pkgname = "gitui"
pkgver = "0.27.0"
pkgrel = 1
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=ghemoji,regex-onig,vendor-openssl",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Terminal ui for git"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/extrawurst/gitui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "55a85f4a3ce97712b618575aa80f3c15ea4004d554e8899669910d7fb4ff6e4b"
env = {"GITUI_RELEASE": "1"}

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE.md")
