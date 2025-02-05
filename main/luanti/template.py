pkgname = "luanti"
pkgver = "5.10.0"
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
    "curl-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libpng-devel",
    "libvorbis-devel",
    "libxi-devel",
    "luajit-devel",
    "mesa-devel",
    "ncurses-devel",
    "openal-soft-devel",
    "openssl3-devel",
    "prometheus-cpp-devel",
    "sqlite-devel",
    "zstd-devel",
]
depends = [self.with_pkgver("luanti-common")]
provides = [self.with_pkgver("minetest")]
pkgdesc = "Voxel game creation platform"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://www.luanti.org"
source = (
    f"https://github.com/minetest/minetest/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "2a3161c04e7389608006f01280eda30507f8bacfa1d6b64c2af1b820a62d2677"
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
hardening = ["!int"]
# see below
options = []

if self.profile().arch == "ppc64le":
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
    # dead symlink
    self.uninstall("usr/share/luanti/client/shaders/Irrlicht")


@subpackage("luanti-common")
def _(self):
    self.subdesc = "common files"
    self.provides = [self.with_pkgver("minetest-common")]

    return ["usr/share/luanti/builtin"]


@subpackage("luanti-server")
def _(self):
    self.subdesc = "server"
    self.depends = [self.with_pkgver("luanti-common")]
    self.provides = [self.with_pkgver("minetest-server")]

    return ["usr/bin/luantiserver"]
