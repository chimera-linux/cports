pkgname = "luakit"
pkgver = "2.4.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr", "USE_LUAJIT=1", "DEVELOPMENT_PATHS=0"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "glib-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "lua5.1-luafilesystem",
    "lua5.1-luasocket",
    "luajit-devel",
    "sqlite-devel",
    "webkitgtk-devel",
]
depends = ["luajit", "lua5.1-luafilesystem", "lua5.1-luasocket"]
pkgdesc = "Fast, small, webkit based browser framework extensible by Lua"
license = "GPL-3.0-only"
url = "https://github.com/luakit/luakit"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "65f73939db561de21bba735bdf92c2b32d28c6610e3d114d1420a8477d531802"
# no tests
options = ["!check"]
