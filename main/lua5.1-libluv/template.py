pkgname = "lua5.1-libluv"
pkgver = "1.51.0.1"
pkgrel = 0
_distver = "-".join(pkgver.rsplit(".", 1))
build_style = "cmake"
configure_args = [
    "-DLUA_BUILD_TYPE=System",
    "-DWITH_SHARED_LIBUV=ON",
    "-DBUILD_MODULE=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DWITH_LUA_ENGINE=Lua",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libuv-devel", "lua5.1-devel"]
pkgdesc = "Bare libuv bindings for Lua"
license = "Apache-2.0"
url = "https://github.com/luvit/luv"
source = f"https://github.com/luvit/luv/releases/download/{_distver}/luv-{_distver}.tar.gz"
sha256 = "dc706d9141c185bdce08b6fc8a9d4df05c3ac3676809ee4e9e37e1553d821237"


@subpackage("lua5.1-libluv-devel")
def _(self):
    return self.default_devel()
