pkgname = "opengothic"
pkgver = "1.0.3010"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "glslang-progs", "ninja", "pkgconf", "python"]
makedepends = [
    "doctest",
    "glm",
    "libpng-devel",
    "libpulse-devel",
    "libxcursor-devel",
    "mesa-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl3-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
]
pkgdesc = "Reimplementation of Gothic 2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/Try/OpenGothic"
source = [
    f"{url}//archive/refs/tags/opengothic-v{pkgver}.tar.gz",
    # revisions from the tag
    "https://github.com/bulletphysics/bullet3/archive/ebe1916b90acae8b13cd8c6b637d8327cdc64e94.tar.gz",
    "https://github.com/GothicKit/dmusic/archive/8b43426f3969df9f64d7ff2a5533ee667424c185.tar.gz",
    "https://github.com/schellingb/TinySoundFont/archive/92a8f0e9fe3c98358be7d8564db21fc4b1142d04.tar.gz",
    "https://github.com/GothicKit/ZenKit/archive/257758d266bebdea87d3748715c54b5f850c83e3.tar.gz",
    "https://github.com/Try/Tempest/archive/01e228802bac6eb2e61d46447fb5b9f7356d28b6.tar.gz",
    "https://github.com/lmichaelis/phoenix-libsquish/archive/cc82beff55210816e1bd531fc6057203dc309807.tar.gz",
]
source_paths = [
    ".",
    "lib/bullet3",
    "lib/dmusic",
    "lib/TinySoundFont",
    "lib/ZenKit",
    "lib/Tempest",
    "lib/ZenKit/vendor/libsquish",
]
sha256 = [
    "1f596c809e40e4763d54dd80fe67c58842e26d873c9e340b8639b372fcd70c05",
    "fcb8fc5a628d39f227f7a28cb93b3b3cbab4ad6cb557fa2489160d404d7d75f1",
    "9fd1b3f238f8d679832eb535628787f88ab1fcbba2cd70e7f119d1599b4d2171",
    "c50ba809cd8928e86c66a283b9c979580ce4be9cfb4f96d71de02c1faa737955",
    "680dd838145f8dca5a0b627daaa81a4f913265fd9e8d883112d347e93a8e44dc",
    "16004c21398c49f62cee3234a1c7af2b6f38515be85a56e8cf7bad531a7bb53e",
    "f67e82601beae5af0e6568ecd545a15539e160590ea747b7659f39bd8f37492d",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["!int"]
# no tests
options = ["!check"]


def post_extract(self):
    # nuke vendored libs
    # can't use system openal because tempest uses internal openal stuff
    for lib in ["libpng", "zlib"]:
        self.rm(f"lib/Tempest/Engine/thirdparty/{lib}", recursive=True)


def post_install(self):
    self.uninstall("usr/include")
    self.uninstall("usr/lib/cmake")
    self.uninstall("usr/lib/*.a", glob=True)
    self.install_license("LICENSE")
