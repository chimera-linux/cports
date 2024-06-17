# nb: neovim requires either lua5.1 or luaJIT (a mess)
pkgname = "neovim"
pkgver = "0.10.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "gperf",
    "gettext",
    "lua5.1-bitop",
    "lua5.1-lpeg",
    "lua5.1-libluv",
    "lua5.1-mpack",
]
makedepends = [
    "libuv-devel",
    "libvterm-devel",
    "lua5.1-libluv-devel",
    "msgpack-c-devel",
    "tree-sitter-devel",
    "unibilium-devel",
]
depends = [
    "lua5.1-lpeg",
    "tree-sitter-bash",
    "tree-sitter-c",
    "tree-sitter-lua",
    "tree-sitter-markdown",
    "tree-sitter-python",
    "tree-sitter-query",
    "tree-sitter-vimdoc",
]
ignore_shlibs = ["/usr/lib/lua/5.1/lpeg.so"]
pkgdesc = "Fork of Vim aiming to improve user experience, plugins and GUIs"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0 AND custom:Vim"
url = "https://neovim.io"
source = f"https://github.com/neovim/neovim/archive/v{pkgver}.tar.gz"
sha256 = "372ea2584b0ea2a5a765844d95206bda9e4a57eaa1a2412a9a0726bab750f828"
broken_symlinks = ["usr/share/nvim/runtime/parser"]
# hardening: visibility is needed for "nvim --api-info"
# testing unchecked yet (via "make test", see test/README.md)
options = ["!check"]


match self.profile().arch:
    case "aarch64" | "ppc64le" | "x86_64":
        # ppc64 could work but it misgenerates?
        configure_args += ["-DPREFER_LUA=OFF"]
        hostmakedepends += ["luajit"]
        makedepends += ["luajit-devel"]
    case _:
        configure_args += ["-DPREFER_LUA=ON"]
        hostmakedepends += ["lua5.1"]
        makedepends += ["lua5.1-devel"]


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link(
        "usr/share/nvim/runtime/parser", "../../../lib/tree-sitter"
    )
