pkgname = "impala"
pkgver = "0.4.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI frontend for iwd"
license = "GPL-3.0-only"
url = "https://github.com/pythops/impala"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "cada25ce7f56762f76be232968b878a16dd046939a138d2bd32976b714033fda"
# No tests are available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
