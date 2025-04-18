pkgname = "opentimelineio"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cmake"
# no python bindings because it wants bundled pybind and
# literally noone except kdenlive even uses this thing at all
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DOTIO_FIND_IMATH=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "imath-devel",
]
pkgdesc = "API and interchange format for editorial timeline information"
license = "Apache-2.0"
url = "https://opentimeline.io"
source = [
    f"https://github.com/AcademySoftwareFoundation/OpenTimelineIO/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/Tencent/rapidjson/archive/24b5e7a8b27f42fa16b96fc70aade9106cf7102f.tar.gz",
]
source_paths = [".", "src/deps/rapidjson"]
sha256 = [
    "cdf8281c6091a18a4147295b660e13b610a6d58919a79608bf03e5359c1c2d24",
    "2d2601a82d2d3b7e143a3c8d43ef616671391034bc46891a9816b79cf2d3e7a8",
]


@subpackage("opentimelineio-devel")
def _(self):
    # sigh, unversioned .sos
    self.depends += [self.parent, *makedepends]
    self.file_modes = {
        # cmake targets :/
        "+usr/include/opentimelineio/deps": ("root", "root", 0o755),
    }

    return self.default_devel()
