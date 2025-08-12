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
    "sqlite-devel",
    "webkitgtk-devel",
]
depends = ["lua5.1-luafilesystem", "lua5.1-luasocket"]
pkgdesc = "WebKit-based browser extensible with Lua"
license = "GPL-3.0-or-later"
url = "https://github.com/luakit/luakit"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "65f73939db561de21bba735bdf92c2b32d28c6610e3d114d1420a8477d531802"
# no tests
options = ["etcfiles", "!check"]

match self.profile().arch:
    case "aarch64" | "ppc64le" | "ppc64" | "ppc" | "x86_64":
        make_build_args += ["USE_LUAJIT=1"]
        makedepends += ["luajit-devel"]
    case _:
        make_build_args += ["USE_LUAJIT=0"]
        makedepends += ["lua5.1-devel"]


def post_install(self):
    self.uninstall("usr/share/pixmaps")
    self.install_file("extras/luakit.png", "usr/share/icons/hicolor/64x64/apps")
    self.install_file(
        "extras/luakit.svg", "usr/share/icons/hicolor/scalable/apps"
    )
