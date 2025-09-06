pkgname = "openmw"
pkgver = "0.49.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_OPENCS=ON",
    "-DOPENMW_USE_SYSTEM_BULLET=OFF",
    "-DOPENMW_LTO_BUILD=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools-devel",
]
makedepends = [
    "boost-devel",
    "ffmpeg-devel",
    "libxt-devel",
    "lz4-devel",
    "mygui-devel",
    "openal-soft-devel",
    "openscenegraph-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "sdl2-compat-devel",
    "unshield-devel",
    "yaml-cpp-devel",
]
pkgdesc = "Open implementation of Morrowind's engine"
license = "GPL-3.0-or-later"
url = "https://openmw.org"
# matches the files openmw declares in cmake
_recast_hash = "c393777d26d2ff6519ac23612abf8af42678c9dd"
_bullet_hash = "3.17"
source = [
    f"https://gitlab.com/OpenMW/openmw/-/archive/openmw-{pkgver}/openmw-openmw-{pkgver}.tar.gz",
    f"https://github.com/recastnavigation/recastnavigation/archive/{_recast_hash}.zip",
    f"https://github.com/bulletphysics/bullet3/archive/refs/tags/{_bullet_hash}.tar.gz",
]
source_paths = [
    ".",
    "build/extern/fetched/recastnavigation",
    "build/extern/fetched/bullet",
]
sha256 = [
    "5f31741d61cf7c736bbe522a1a33342773c7e1b713e7e20f3717eb8da2b1733d",
    "7d7fc38c9a52dbda0ba1dab70d1ed59da1178ab1c4fa209cdb7cc2dcfce8e4ea",
    "baa642c906576d4d98d041d0acb80d85dd6eff6e3c16a009b1abf1ccd2bc0a61",
]
# unit tests are off
# FIXME lintpixmaps
options = ["!check", "!lintpixmaps"]

if self.profile().endian == "big":
    broken = "esm loader is not ready etc."

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["luajit-devel"]
else:
    makedepends += ["lua5.1-devel"]
    configure_args += ["-DUSE_LUAJIT=OFF"]


@subpackage("openmw-cs")
def _(self):
    self.pkgdesc = "Open implementation of Morrowind Creation Set"
    self.depends = [self.parent]
    # FIXME lintpixmaps
    self.options = ["!lintpixmaps"]

    return [
        "etc/openmw/defaults-cs.bin",
        "usr/bin/openmw-cs",
        "usr/share/applications/org.openmw.cs.desktop",
        "usr/share/pixmaps/openmw-cs.png",
    ]


@subpackage("openmw-esmtool")
def _(self):
    self.pkgdesc = "Tool for inspecting and extracitng Morrowind ESM files"
    # transitional
    self.provides = [self.with_pkgver("esmtool")]

    return ["usr/bin/esmtool"]


@subpackage("openmw-bsatool")
def _(self):
    self.pkgdesc = "Tool for inspecting Bethesda BSA archives"
    # transitional
    self.provides = [self.with_pkgver("esmtool")]

    return ["usr/bin/bsatool"]
