pkgname = "tokei"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cargo"
# we patch lockfile
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libgit2-devel"]
pkgdesc = "CLI for counting lines of code with stats per language"
license = "Apache-2.0 OR MIT"
url = "https://github.com/XAMPPRocky/tokei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "966da7b9a81ac6cb777b9f159f4c02e5b83a8b8bd30ebf5991007839926b600c"


def post_install(self):
    self.install_license("LICENCE-MIT")
