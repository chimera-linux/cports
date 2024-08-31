pkgname = "tmux-sessionizer"
pkgver = "0.4.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl-devel", "libgit2-devel"]
pkgdesc = "Tool for opening git repositories as tmux sessions"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jrmoulton/tmux-sessionizer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e7baf324409af475a96d2b034a2ecdb46452feb7d0ef3ddc41e834475063a1f7"


def post_install(self):
    self.install_license("LICENSE")
