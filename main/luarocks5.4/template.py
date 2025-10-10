pkgname = "luarocks5.4"
pkgver = "3.12.2"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--lua-version=5.4",
    "--prefix=/usr",
]
hostmakedepends = ["lua5.4", "unzip"]
makedepends = ["lua5.4-devel"]
depends = ["lua5.4-devel", "unzip"]
pkgdesc = "Package manager for Lua modules"
license = "MIT"
url = "https://luarocks.org"
source = f"{url}/releases/luarocks-{pkgver}.tar.gz"
sha256 = "b0e0c85205841ddd7be485f53d6125766d18a81d226588d2366931e9a1484492"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
