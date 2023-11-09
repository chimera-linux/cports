pkgname = "audacity"
pkgver = "3.4.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # release
    "-DAUDACITY_BUILD_LEVEL=2",
    # autofetch
    "-Daudacity_conan_enabled=OFF",
    # telemetry
    "-Daudacity_has_crashreports=OFF",
    "-Daudacity_has_networking=OFF",
    "-Daudacity_has_sentry_reporting=OFF",
    "-Daudacity_has_updates_check=OFF",
    # todo: weird ass sdk
    "-Daudacity_has_vst3=OFF",
    "-Daudacity_lib_preference=system",
    "-Daudacity_obey_system_dependencies=ON",
    # doesn't work with system version
    "-Daudacity_use_portsmf=local",
]
hostmakedepends = [
    "cmake",
    "nasm",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "ffmpeg-devel",
    "gtk+3-devel",
    "lame-devel",
    "libexpat-devel",
    "libid3tag-devel",
    "libogg-devel",
    "libsbsms-devel",
    "libsndfile-devel",
    "libuuid-devel",
    "libvorbis-devel",
    "lilv-devel",
    "lv2",
    "mpg123-devel",
    "opusfile-devel",
    "pipewire-jack-devel",
    "portaudio-devel",
    "portmidi-devel",
    "rapidjson",
    "soundtouch-devel",
    "soxr-devel",
    "sqlite-devel",
    "suil-devel",
    "taglib-devel",
    "twolame-devel",
    "vamp-plugin-sdk-devel",
    "wavpack-devel",
    "wxwidgets-devel",
    "zlib-devel",
]
pkgdesc = "Multitrack audio editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.audacityteam.org"
source = f"https://github.com/audacity/audacity/releases/download/Audacity-{pkgver}/audacity-sources-{pkgver}.tar.gz"
sha256 = "4e902a2624cdca5f4e95a19a89f27bc2150463f17a5eacb7cd3ca677d410762b"
# vis breaks symbols
hardening = []
# check: dont care
options = ["!check", "linkundefver"]

tool_flags = {
    # disarm debug
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        "-DNDEBUG",
        # stfu
        "-Wno-deprecated-declarations",
        "-Wno-deprecated-non-prototype",
        "-Wno-unqualified-std-cast-call",
    ],
}

if self.profile().endian == "big":
    broken = "unimplemented bits"
