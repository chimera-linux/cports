# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "neovim"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DPREFER_LUA=on",
    f"-DLUA_INCLUDE_DIR={self.profile().sysroot / 'usr/include/lua5.1'}",
    f"-DLUA_LIBRARIES={self.profile().sysroot / 'usr/lib/lua/5.1'}",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "gperf",
    "gettext-tiny",
    "lua5.1-bitop",
    "lua5.1-lpeg",
    "lua5.1-libluv",
    "lua5.1-mpack",
]
makedepends = [
    "unibilium-devel",
    "libtermkey-devel",
    "libvterm-devel",
    "lua5.1-devel",
    "libuv-devel",
    "lua5.1-libluv-devel",
    "msgpack-c-devel",
    "tree-sitter-devel",
]
pkgdesc = "Fork of Vim aiming to improve user experience, plugins and GUIs"
license = "Apache-2.0 AND custom:Vim"
url = "https://neovim.io"
source = f"https://github.com/neovim/neovim/archive/v{pkgver}.tar.gz"
sha256 = "39d79107c54d2f3babcad2cd157c399241c04f6e75e98c18e8afaf2bb5e82937"
# hardening: visibility is needed for "nvim --api-info"
# testing unchecked yet (via "make test", see test/README.md)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
