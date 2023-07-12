pkgname = "lua5.1-libluv"
pkgver = "1.45.0.0"
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
sha256 = "fa6c46fb09f88320afa7f88017efd7b0d2b3a0158c5ba5b6851340b0332a2b81"
# no tests provided by upstream
options = ["!check"]


@subpackage("lua5.1-libluv-devel")
def _devel(self):
    return self.default_devel()
