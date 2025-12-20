pkgname = "comrak"
pkgver = "0.49.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0ce97f37c67fca030d70b8736cd9ca37e3b5b0685d4e003412b1534f074ca122"

if self.profile().arch in ["loongarch64"]:
    broken = "linux-raw-sys does not support, can't bump (semver)"


def post_install(self):
    self.install_license("COPYING")
