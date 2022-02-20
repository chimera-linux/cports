pkgname = "lua5.1-lgi"
pkgver = "0.9.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["LUA_VERSION=5.1", "LUA_CFLAGS=-I/usr/include/lua5.1"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "gmake", "glib-devel", "libffi-devel", "lua5.1-devel", "gobject-introspection",
    "gir-freedesktop"
]
depends = ["gir-freedesktop"]
pkgdesc = "Lua binding to GObject libraries using GObject-Introspection"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/lgi-devs/lgi"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cfc4105482b4730b3a40097c9d9e7e35c46df2fb255370bdeb2f45a886548c4f"
# requires X
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
