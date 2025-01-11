pkgname = "zvm"
pkgver = "0.8.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e2efbb886aabe9e11ae9016fe292ee066ab2953c2eb366aa76b642a810366864"


def post_install(self):
    self.install_license("LICENSE")
