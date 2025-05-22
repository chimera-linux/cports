pkgname = "tmux-sessionizer"
pkgver = "0.4.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "libgit2-devel"]
pkgdesc = "Tool for opening git repositories as tmux sessions"
license = "MIT"
url = "https://github.com/jrmoulton/tmux-sessionizer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "37cceae77bad373452d08b990065e7d1e8ed7b038a0af126aa4403332364530e"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
