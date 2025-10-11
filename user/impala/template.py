pkgname = "impala"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6ebdfbd83f7c3874fd43a1b781a7c08b309a2dc5bef99e1c29c5736b616a0f33"
# No tests are available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
