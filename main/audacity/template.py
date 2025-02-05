pkgname = "audacity"
pkgver = "3.7.1"
pkgrel = 1
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
    "twolame-devel",
    "util-linux-uuid-devel",
    "vamp-plugin-sdk-devel",
    "wavpack-devel",
    "wxwidgets-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Multitrack audio editor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.audacityteam.org"
source = f"https://github.com/audacity/audacity/releases/download/Audacity-{pkgver}/audacity-sources-{pkgver}.tar.gz"
sha256 = "5f89397a60dee54e5a6b05c9947ebce6e1566815050b01c534c52d44353ceb80"
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
