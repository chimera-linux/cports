pkgname = "qt6-qtwebengine"
pkgver = "6.7.1"
pkgrel = 1
archs = ["aarch64", "ppc64le", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DINSTALL_ARCHDATADIR=lib/qt6",
    "-DINSTALL_BINDIR=lib/qt6/bin",
    "-DINSTALL_DATADIR=share/qt6",
    "-DINSTALL_DOCDIR=share/doc/qt6",
    "-DINSTALL_EXAMPLESDIR=share/doc/qt6/examples",
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
hostmakedepends = [
    "cmake",
    "bison",
    "flex",
    "gperf",
    # for gn
    "libcxx-devel-static",
    "ninja",
    "nodejs",
    "perl",
    "pkgconf",
    "python",
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
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebengine-everywhere-src-{pkgver}.tar.xz"
sha256 = "53f08012609a7d949b0e951728ac2364a06466325ffd163b56a87c3fd021dc44"
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


def post_install(self):
    self.rm(self.destdir / "usr/lib/qt6/bin/testbrowser")
    self.rm(self.destdir / "usr/lib/qt6/libexec/gn")


@subpackage("qt6-qtwebengine-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
