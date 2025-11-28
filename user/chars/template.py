pkgname = "chars"
pkgver = "0.7.0"
pkgrel = 0
build_wrksrc = "chars"
build_style = "cargo"
# lockfile is patched
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["git"]
pkgdesc = "Tool to display information about Unicode characters"
license = "MIT"
url = "https://github.com/boinkor-net/chars"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2f79843a3b1173870b41ebce491a54812b13a44090d0ae30a6f572caa91f0736"


def post_install(self):
    self.install_license("../LICENSE")
