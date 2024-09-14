pkgname = "lua5.4-luaexpat"
pkgver = "1.5.2"
pkgrel = 0
build_style = "makefile"
make_dir = "."
makedepends = ["libexpat-devel", "lua5.4-devel"]
pkgdesc = "SAX XML parser based on the Expat library"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://lunarmodules.github.io/luaexpat"
source = f"https://github.com/lunarmodules/luaexpat/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "89d83f2141edec31be576425637216928221918fe95dc3854d1b7fd4c627213f"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
