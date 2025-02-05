pkgname = "openmw"
pkgver = "0.47.0"
pkgrel = 9
build_style = "cmake"
configure_args = [
    # enable once we have proper qt6 support (0.49)
    "-DBUILD_OPENCS=OFF",
    "-DOPENMW_USE_SYSTEM_BULLET=OFF",
    "-DOPENMW_LTO_BUILD=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
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
    "sdl2-compat-devel",
    "unshield-devel",
]
pkgdesc = "Open implementation of Morrowind's engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://openmw.org"
# matches the files openmw declares in cmake
_recast_hash = "e75adf86f91eb3082220085e42dda62679f9a3ea"
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
    "bd7f77e1527c2180e9b0dfcbe401d6fb48f24dbb37701dac7747697873d6edb4",
    "d3339aaea1d81307bcac2bece176c5359ed5f8c8f9721fc360d28f82f9119253",
    "baa642c906576d4d98d041d0acb80d85dd6eff6e3c16a009b1abf1ccd2bc0a61",
]
# unit tests are off
options = ["!check"]

if self.profile().endian == "big":
    broken = "esm loader is not ready etc."


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
