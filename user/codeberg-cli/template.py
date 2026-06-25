pkgname = "codeberg-cli"
pkgver = "0.5.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "libgit2-devel"]
pkgdesc = "CLI Tool for Codeberg similar to gh and glab"
license = "AGPL-3.0-only"
url = "https://codeberg.org/Aviac/codeberg-cli"
source = (
    f"https://codeberg.org/Aviac/codeberg-cli/archive/v{pkgver}.tar.gz"
)
sha256 = "6f91dd631ec630d7b558abcc783757ea189e934aee5ea645691268f859d0c197"

def post_install(self):
    self.install_license("LICENSE")
