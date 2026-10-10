pkgname = "vivid"
pkgver = "0.11.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Themeable LS_COLORS generator"
license = "MIT AND Apache-2.0"
url = "https://github.com/sharkdp/vivid"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a43ccfbc6554055181a08f2740664f9280fa2d0e57c4641850c60dd0e5323720"


def post_install(self):
    self.install_license("LICENSE-MIT")
