pkgname = "comrak"
pkgver = "0.52.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2321a3f9f23feae95402234fa02e71cad2a902583fdfa7097b7da0717fdad49b"


def post_install(self):
    self.install_license("COPYING")
