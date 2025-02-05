pkgname = "lua5.1-lgi"
pkgver = "0.9.2"
pkgrel = 1
build_style = "makefile"
make_build_args = ["LUA_VERSION=5.1", "LUA_CFLAGS=-I/usr/include/lua5.1"]
make_check_args = ["LUA=lua5.1"]
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = ["pkgconf", "gobject-introspection"]
makedepends = [
    "gobject-introspection-freedesktop",
    "glib-devel",
    "libffi8-devel",
    "lua5.1-devel",
]
depends = ["gobject-introspection-freedesktop"]
checkdepends = ["xwayland-run", "dbus", "lua5.1", "gtk+3"]
pkgdesc = "Lua binding to GObject libraries using GObject-Introspection"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/lgi-devs/lgi"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cfc4105482b4730b3a40097c9d9e7e35c46df2fb255370bdeb2f45a886548c4f"


def post_install(self):
    self.install_license("LICENSE")
