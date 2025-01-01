pkgname = "gitui"
pkgver = "0.26.3"
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
    "openssl-devel",
    "rust-std",
]
pkgdesc = "Terminal ui for git"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/extrawurst/gitui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8075e180f3b01ff0c290b690488a7628c44b4de12346e04a77d823914a48918b"
env = {"GITUI_RELEASE": "1"}

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE.md")
