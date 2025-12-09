pkgname = "tokei"
pkgver = "13.0.0"
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
sha256 = "b426ab03b8eedf4fe3ea70ca8379a2355981b0e9ca1d0083a66e623858e7e481"


def post_install(self):
    self.install_license("LICENCE-MIT")
