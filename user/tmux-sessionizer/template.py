pkgname = "tmux-sessionizer"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for opening git repositories as tmux sessions"
license = "MIT"
url = "https://github.com/jrmoulton/tmux-sessionizer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c3205764f70c8e7f94a1b32eccbc22e402cd9ab28c54d06b405073cae185bdd8"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
