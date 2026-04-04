pkgname = "toml-bombadil"
pkgver = "4.2.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # bwrap issues
    "--skip=git::test::should_clone_repository",
    # needs network
    "--skip=gpg::test::should_encrypt",
]
hostmakedepends = ["cargo", "gnupg", "pkgconf"]
makedepends = ["libgit2-devel", "openssl3-devel"]
depends = ["gnupg"]
pkgdesc = "Dotfile manager program"
license = "MIT"
url = "https://oknozor.github.io/toml-bombadil"
source = f"https://github.com/oknozor/toml-bombadil/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b911678642a1229908dfeabbdd7f799354346c0e37f3ac999277655e01b6f229"


def post_install(self):
    self.install_license("LICENSE")
