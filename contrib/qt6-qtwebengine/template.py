pkgname = "qt6-qtwebengine"
pkgver = "6.7.2"
pkgrel = 1
# latest from https://github.com/qt/qtwebengine-chromium/commits/118-based
# check CHROMIUM_VERSION on qt majors
_qtwebengine_gitrev = "7d28f93db7534943f84c5e6cab7778b83e1d2c3b"
archs = ["aarch64", "ppc64le", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DINSTALL_ARCHDATADIR=lib/qt6",
    "-DINSTALL_BINDIR=lib/qt6/bin",
    "-DINSTALL_DATADIR=share/qt6",
    "-DINSTALL_DOCDIR=share/doc/qt6",
    "-DINSTALL_EXAMPLESDIR=share/doc/qt6/examples",
    "-DINSTALL_GN=OFF",
    "-DINSTALL_INCLUDEDIR=include/qt6",
    "-DINSTALL_MKSPECSDIR=lib/qt6/mkspecs",
    "-DQT_FEATURE_webengine_kerberos=ON",
    "-DQT_FEATURE_webengine_proprietary_codecs=ON",
    "-DQT_FEATURE_webengine_system_alsa=ON",
    "-DQT_FEATURE_webengine_system_ffmpeg=ON",
    "-DQT_FEATURE_webengine_system_icu=ON",
    "-DQT_FEATURE_webengine_system_libevent=ON",
    "-DQT_FEATURE_webengine_system_libpci=ON",
    "-DQT_FEATURE_webengine_system_libpng=ON",
    "-DQT_FEATURE_webengine_system_libwebp=ON",
    "-DQT_FEATURE_webengine_system_libxml=ON",
    "-DQT_FEATURE_webengine_system_minizip=ON",
    "-DQT_FEATURE_webengine_system_opus=ON",
    "-DQT_FEATURE_webengine_system_pulseaudio=ON",
    "-DQT_FEATURE_webengine_system_zlib=ON",
    "-DQT_FEATURE_webengine_webrtc_pipewire=ON",
]
configure_env = {
    "EXTRA_GN": "link_pulseaudio=true"
    + " rtc_link_pipewire=true"
    + " symbol_level=1"
    + " use_dwarf5=true"
}
hostmakedepends = [
    "cmake",
    "bison",
    "flex",
    "gperf",
    "ninja",
    "nodejs",
    "perl",
    "pkgconf",
    "python-html5lib",
    "qt6-qtbase",
]
makedepends = [
    "alsa-lib-devel",
    "brotli-devel",
    "bzip2-devel",
    "cairo-devel",
    "ffmpeg-devel",
    "freetype-devel",
    "heimdal-devel",
    "icu-devel",
    "lcms2-devel",
    "libevent-devel",
    "libpulse-devel",
    "libva-devel",
    "libwebp-devel",
    "libxkbfile-devel",
    "libxshmfence-devel",
    "libxslt-devel",
    "minizip-devel",
    "musl-bsd-headers",
    "nss-devel",
    "opus-devel",
    "pciutils-devel",
    "pipewire-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "qt6-qtwebchannel-devel",
    "qt6-qtwebsockets-devel",
    "snappy-devel",
]
depends = ["hwdata-usb"]
pkgdesc = "Qt6 webengine component"
maintainer = "psykose <alice@ayaya.dev>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = [
    f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebengine-everywhere-src-{pkgver}.tar.xz",
    f"https://github.com/qt/qtwebengine-chromium/archive/{_qtwebengine_gitrev}.tar.gz",
]
source_paths = [".", "3rdparty-chromium"]
sha256 = [
    "c7755875594d8be382b07bf3634d44fd77012805794d8b588891709a6405ffd1",
    "edb36db47bc288ad698e57db1ebcc448664faebbc350e8b40663c7eed283b40a",
]
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "CFLAGS": [
        "-Wno-unknown-warning-option",
        "-Wno-builtin-macro-redefined",
        "-Wno-deprecated-declarations",
    ],
    "CXXFLAGS": [
        "-Wno-unknown-warning-option",
        "-Wno-builtin-macro-redefined",
        "-Wno-deprecated-declarations",
    ],
}
hardening = ["!int", "!scp"]
# lol
options = ["!check", "!cross"]


def post_extract(self):
    # nuke old chromium tree to replace with the updated one
    self.rm("src/3rdparty", recursive=True)
    self.mv("3rdparty-chromium", "src/3rdparty")


def post_install(self):
    self.uninstall("usr/lib/qt6/bin/testbrowser")


@subpackage("qt6-qtwebengine-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/qt6/plugins/designer",
            "usr/lib/*.prl",
        ]
    )
