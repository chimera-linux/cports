pkgname = "impala"
pkgver = "0.7.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["iwd"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "948b9b46ee7b8c06016430bc0e9fef8a23ecf9768cfe11ec1f9fd48dde249bb2"


def post_install(self):
    self.install_license("LICENSE")
