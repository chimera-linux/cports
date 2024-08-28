pkgname = "lua5.4-lua_cliargs"
pkgver = "3.0.2"
pkgrel = 0
pkgdesc = "CLI argument parsing module for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/lunarmodules/lua_cliargs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a7a57ab9c73f6c44040a78305b6dc7780ca1565cc4c9057d74a6608cb0443af4"


def install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/share/lua/5.4")
    self.install_file("src/cliargs.lua", "usr/share/lua/5.4")
    self.install_files("src/cliargs", "usr/share/lua/5.4")
