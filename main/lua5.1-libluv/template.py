pkgname = "lua5.1-libluv"
pkgver = "1.50.0.1"
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
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0"
url = "https://github.com/luvit/luv"
source = f"https://github.com/luvit/luv/releases/download/{_distver}/luv-{_distver}.tar.gz"
sha256 = "d867c3024d9c981d54f2edd83e13fd6dc1158f0608635f7b1c0f6b5586b5bc34"


@subpackage("lua5.1-libluv-devel")
def _(self):
    return self.default_devel()
