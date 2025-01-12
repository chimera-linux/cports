pkgname = "comrak"
pkgver = "0.33.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "52f3a8aa79dbde40c3a3f8ea540098150a2b7049cb30f41ec32ea56399dd8c81"


def post_install(self):
    self.install_license("COPYING")
