pkgname = "luanti"
pkgver = "5.17.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SERVER=TRUE",
    # passed manually
    "-DENABLE_LTO=OFF",
    "-DENABLE_PROMETHEUS=ON",
    "-DENABLE_UPDATE_CHECKER=OFF",
    "-DUSE_SDL2=OFF",
    "-DUSE_SDL3=ON",
]
hostmakedepends = [
    "cmake",
    "doxygen",
    "gettext-devel",
    "graphviz",
    "ninja",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "curl-devel",
    "freetype-devel",
    "gettext-devel",
    "gmp-devel",
    "hiredis-devel",
    "jsoncpp-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libpng-devel",
    "libvorbis-devel",
    "luajit-devel",
    "mesa-devel",
    "ncurses-devel",
    "openal-soft-devel",
    "openssl3-devel",
    "prometheus-cpp-devel",
    "sdl3-devel",
    "sqlite-devel",
    "zstd-devel",
]
depends = [self.with_pkgver("luanti-common")]
renames = ["minetest"]
pkgdesc = "Voxel game creation platform"
license = "LGPL-2.1-or-later"
url = "https://www.luanti.org"
source = (
    f"https://github.com/luanti-org/luanti/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "52e7dd315ae0e5c3868a23231e691578cd694bcca5af627fc57c03f32bdc846f"
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
hardening = ["!int"]
# see below
options = ["etcfiles"]

if self.profile.arch == "ppc64le":
    # FIXME: testLuaDestructors fails since luajit seems to not unwind destructors on ppc64le
    options += ["!check"]


def check(self):
    self.do("bin/luanti", "--run-unittests")
    self.do("bin/luantiserver", "--run-unittests")


def post_install(self):
    self.install_file(
        "minetest.conf.example",
        "etc/luanti",
        name="minetest.conf",
    )


@subpackage("luanti-common")
def _(self):
    self.subdesc = "common files"
    self.renames = ["minetest-common"]

    return ["usr/share/luanti/builtin"]


@subpackage("luanti-server")
def _(self):
    self.subdesc = "server"
    self.depends = [self.with_pkgver("luanti-common")]
    self.renames = ["minetest-server"]

    return ["usr/bin/luantiserver"]
