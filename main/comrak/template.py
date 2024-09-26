pkgname = "comrak"
pkgver = "0.28.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7e1ef40ebf2a27faaad7c2068e32d2109726f6daf42ba64705e7a250a9b0a162"


def post_install(self):
    self.install_license("COPYING")
