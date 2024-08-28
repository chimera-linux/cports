pkgname = "lua5.4-say"
pkgver = "1.4.1"
pkgrel = 0
pkgdesc = "Lua string hashing library, useful for internationalization"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/lunarmodules/say"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ce07547ca49ef42cc799e2a30b3c65ce77039978e32e7961799a252d61a56486"


def install(self):
    self.install_files("src/say", "usr/share/lua/5.4")
    self.install_license("LICENSE")
