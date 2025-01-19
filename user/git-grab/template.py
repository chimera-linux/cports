pkgname = "git-grab"
pkgver = "3.0.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["git"]
pkgdesc = "Clone a git repository into a standard location"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Apache-2.0"
url = "https://github.com/wezm/git-grab"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "542a1e1c1d2a3f1f073e23817bfbab1b98f352f590991e50c6a484177a724b95"


def post_install(self):
    self.install_license("LICENSE-MIT")
