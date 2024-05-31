pkgname = "comrak"
pkgver = "0.24.1"
pkgrel = 0
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "045aadd282968c15499bf308974fb9ea4293b9b8ada29baaafa818546943297d"


def post_install(self):
    self.install_license("COPYING")
