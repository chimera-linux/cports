pkgname = "lua5.4-busted"
pkgver = "2.2.0"
pkgrel = 0
depends = [
    "lua5.4-lua_cliargs",
    "lua5.4-mediator_lua",
    "lua5.4-penlight",
    "lua5.4-luassert",
    "lua5.4-luasystem",
    "lua5.4-lua-term",
]
pkgdesc = "Lua unit testing"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://lunarmodules.github.io/busted"
source = (
    f"https://github.com/lunarmodules/busted/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "befca10f573bb476fa1db2e3149150d65f802a71d34d1682679e640665f2dc2b"


def do_install(self):
    self.install_bin("bin/busted")
    self.install_files("busted", "usr/share/lua/5.4")
    self.install_completion("completions/bash/busted.bash", "bash")
    self.install_completion("completions/zsh/_busted", "zsh")
    self.install_license("LICENSE")
