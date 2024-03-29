pkgname = "git-grab"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["git"]
pkgdesc = "Clone a git repository into a standard location"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT OR Apache-2.0"
url = "https://github.com/wezm/git-grab"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ae9edda2d9ff499d2282035e84fa3d5da3776fab1a36e1922dce9584222a196a"


def post_install(self):
    self.install_license("LICENSE-MIT")
