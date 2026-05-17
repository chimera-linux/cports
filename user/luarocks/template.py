pkgname = "luarocks"
pkgver = "3.12.2"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--rocks-tree=/usr/lib/luarocks",
]
hostmakedepends = ["unzip"]
makedepends = ["lua5.1-devel"]
depends = ["lua5.1"]
pkgdesc = "Package manager for Lua modules"
license = "MIT"
url = "https://luarocks.org"
source = f"{url}/releases/luarocks-{pkgver}.tar.gz"
sha256 = "b0e0c85205841ddd7be485f53d6125766d18a81d226588d2366931e9a1484492"
# not implemented
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
