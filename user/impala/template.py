pkgname = "impala"
pkgver = "0.2.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "550ce667588659af40ff2af6bddcca74fb1a990001ccba7cf16d3739717a70fc"
# No tests are available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
