pkgname = "toml-bombadil"
pkgver = "4.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["gnupg", "libgit2-devel", "openssl3-devel"]
depends = ["gnupg"]
pkgdesc = "Dotfile manager written in Rust"
license = "MIT"
url = "https://oknozor.github.io/toml-bombadil"
source = f"https://github.com/oknozor/toml-bombadil/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b911678642a1229908dfeabbdd7f799354346c0e37f3ac999277655e01b6f229"
# Needs network access during check phase and weird permission problems when
# running gpg in the bubblewrap container. All other tests pass though
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
