pkgname = "impala"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "26d825176e1a3c9ebcc94d874580807be8a6e3c3ea4beef8170a8604ef4b0c5c"
# No tests are available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
