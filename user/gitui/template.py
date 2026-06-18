pkgname = "gitui"
pkgver = "0.28.1"
pkgrel = 0
build_style = "cargo"
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
license = "MIT"
url = "https://github.com/extrawurst/gitui"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0400cbf59605490b5fb8779f9af41fa4d7a1bb748093ca0e13156a5dff31c7aa"
env = {"GITUI_RELEASE": "1"}

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "libc-0.2.180")


def post_install(self):
    self.install_license("LICENSE.md")
