pkgname = "minetest"
pkgver = "5.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SERVER=TRUE",
    # passed manually
    "-DENABLE_LTO=OFF",
    "-DENABLE_PROMETHEUS=ON",
    "-DENABLE_UPDATE_CHECKER=OFF",
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
    "freetype-devel",
    "gettext-devel",
    "gmp-devel",
    "hiredis-devel",
    "jsoncpp-devel",
    "libcurl-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libpng-devel",
    "libvorbis-devel",
    "libxi-devel",
    "luajit-devel",
    "mesa-devel",
    "ncurses-devel",
    "openal-soft-devel",
    "openssl-devel",
    "prometheus-cpp-devel",
    "sqlite-devel",
    "zstd-devel",
]
depends = [self.with_pkgver("minetest-common")]
pkgdesc = "Voxel game creation platform"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://www.minetest.net"
source = (
    f"https://github.com/minetest/minetest/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "070bc292a0b7fc60d7ff0a14b364c8229c5cbe38296a80f948ea2c2591545a5c"
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
hardening = ["!int"]
# see below
options = []

if self.profile().arch == "ppc64le":
    # FIXME: testLuaDestructors fails since luajit seems to not unwind destructors on ppc64le
    options += ["!check"]


def check(self):
    self.do("bin/minetest", "--run-unittests")
    self.do("bin/minetestserver", "--run-unittests")


def post_install(self):
    self.install_file(
        "minetest.conf.example",
        "etc/minetest",
        name="minetest.conf",
    )
    # dead symlink
    self.uninstall("usr/share/minetest/client/shaders/Irrlicht")


@subpackage("minetest-common")
def _(self):
    self.subdesc = "common files"

    return ["usr/share/minetest/builtin"]


@subpackage("minetest-server")
def _(self):
    self.subdesc = "server"
    self.depends = [self.with_pkgver("minetest-common")]

    return ["usr/bin/minetestserver"]
