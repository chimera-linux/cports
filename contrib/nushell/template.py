pkgname = "nushell"
pkgver = "0.96.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "openssl-devel", "sqlite-devel", "zstd-devel"]
pkgdesc = "Shell with a focus on structured data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ed3035487b2f6eed0a958532edd68a379617649a9381480726265f15dd6eabad"
# Checks fail with libgit2 < 1.8.1
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
