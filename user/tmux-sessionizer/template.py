pkgname = "tmux-sessionizer"
pkgver = "0.4.4"
pkgrel = 2
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "libgit2-devel"]
pkgdesc = "Tool for opening git repositories as tmux sessions"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jrmoulton/tmux-sessionizer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9dfbe99a3c1fe7f48be0c1ab9056e49f36c4f85d023e24f874254f6791a9894e"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
