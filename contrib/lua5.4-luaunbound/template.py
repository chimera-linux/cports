pkgname = "lua5.4-luaunbound"
pkgver = "1.0.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LUA_VERSION=5.4"]
make_install_args = [*make_build_args]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "lua5.4-devel",
    "unbound-devel",
]
pkgdesc = "Lua bindings to libunbound"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://www.zash.se/luaunbound.html"
source = f"https://code.zash.se/dl/luaunbound/luaunbound-{pkgver}.tar.gz"
sha256 = "6de45aa64c21cf0ecbccb734b7c1eda8873a6135bbe142fbf353f772a90750d3"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
