pkgname = "lua5.1-libluv"
pkgver = "1.48.0.2"
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
sha256 = "2c3a1ddfebb4f6550293a40ee789f7122e97647eede51511f57203de48c03b7a"


@subpackage("lua5.1-libluv-devel")
def _(self):
    return self.default_devel()
