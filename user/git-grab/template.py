pkgname = "git-grab"
pkgver = "4.0.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["git"]
pkgdesc = "Clone a git repository into a standard location"
license = "MIT OR Apache-2.0"
url = "https://github.com/wezm/git-grab"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "63c080d78dd1d5213b59ae0b98418b9f374c59ccfaa444c55e99b7004fd4fe13"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_man("git-grab.1")
