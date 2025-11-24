pkgname = "comrak"
pkgver = "0.48.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "91d136008082a5019df88255bef198e21f177cf7234895be4957ffeb92bd886e"

if self.profile().arch in ["loongarch64"]:
    broken = "linux-raw-sys does not support, can't bump (semver)"


def post_install(self):
    self.install_license("COPYING")
