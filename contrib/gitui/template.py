pkgname = "gitui"
pkgver = "0.26.2"
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
sha256 = "c69eccba2457c53c18b933794aa4ff3dfecb71af42349282108354d543e4d956"
env = {"GITUI_RELEASE": "1"}


def post_install(self):
    self.install_license("LICENSE.md")
