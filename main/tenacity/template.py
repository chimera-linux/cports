pkgname = "tenacity"
pkgver = "1.3.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # release
    "-DTENACITY_BUILD_LEVEL=2",
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
    "libmatroska-devel",
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
    "portsmf-devel",
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
depends = ["ffmpeg-avcodec-libs"]
# switch people over because we don't ship this anymore
renames = ["audacity=3.7.7-r1"]
pkgdesc = "Multitrack audio editor"
license = "GPL-3.0-or-later"
url = "https://tenacityaudio.org"
source = f"https://codeberg.org/tenacityteam/tenacity/releases/download/v{pkgver}/tenacity-{pkgver}-src.tar.gz"
sha256 = "0446e14e09046a0c72d0fdfbbf3823a2ba3451204de7b93f715cc4fe2333e781"
# vis breaks symbols
hardening = []
# check: dont care
# no need to scan for library providers, we don't have a devel package
options = ["!check", "linkundefver", "!scanshlibs"]

tool_flags = {
    # disarm debug
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        "-DNDEBUG",
        # stfu
        "-Wno-deprecated-declarations",
        "-Wno-deprecated-non-prototype",
        "-Wno-inconsistent-missing-override",
        "-Wno-macro-redefined",
        "-Wno-unqualified-std-cast-call",
    ],
}

if self.profile().endian == "big":
    broken = "unimplemented bits"


def post_extract(self):
    # leftover
    self.rm(".git")


def post_install(self):
    self.uninstall("usr/share/pixmaps")
