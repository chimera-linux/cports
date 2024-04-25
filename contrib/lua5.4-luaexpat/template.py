pkgname = "lua5.4-luaexpat"
pkgver = "1.5.1"
pkgrel = 0
build_style = "makefile"
make_dir = "."
makedepends = ["libexpat-devel", "lua5.4-devel"]
pkgdesc = "SAX XML parser based on the Expat library"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://lunarmodules.github.io/luaexpat"
source = f"https://github.com/lunarmodules/luaexpat/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7d455f154de59eb0b073c3620bc8b873f7f697b3f21a112e6ff8dc9fca6d0826"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
