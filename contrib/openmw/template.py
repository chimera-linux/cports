pkgname = "openmw"
pkgver = "0.47.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    # enable once we have proper qt6 support (0.49)
    "-DBUILD_OPENCS=OFF",
    "-DOPENMW_USE_SYSTEM_BULLET=OFF",
    "-DOPENMW_LTO_BUILD=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qttools", "qt6-qtbase"]
makedepends = [
    "sdl-devel",
    "boost-devel",
    "ffmpeg-devel",
    "mygui-devel",
    "lz4-devel",
    "openscenegraph-devel",
    "unshield-devel",
    "openal-soft-devel",
    "qt6-qtbase-devel",
    "libxt-devel",
]
pkgdesc = "Open implementation of Morrowind's engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://openmw.org"
# matches the files openmw declares in cmake
_recast_hash = "e75adf86f91eb3082220085e42dda62679f9a3ea"
_bullet_hash = "3.17"
source = [
    f"https://gitlab.com/OpenMW/openmw/-/archive/{pkgname}-{pkgver}/{pkgname}-{pkgname}-{pkgver}.tar.gz",
    f"!https://github.com/recastnavigation/recastnavigation/archive/{_recast_hash}.zip",
    f"!https://github.com/bulletphysics/bullet3/archive/refs/tags/{_bullet_hash}.tar.gz",
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


def post_extract(self):
    self.cp(self.sources_path / f"{_recast_hash}.zip", ".")
    self.cp(self.sources_path / f"{_bullet_hash}.tar.gz", ".")


@subpackage("esmtool")
def _esmtool(self):
    self.pkgdesc = "Tool for inspecting and extracitng Morrowind ESM files"

    return ["usr/bin/esmtool"]


@subpackage("bsatool")
def _bsatool(self):
    self.pkgdesc = "Tool for inspecting Bethesda BSA archives"

    return ["usr/bin/bsatool"]
