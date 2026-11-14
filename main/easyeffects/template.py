pkgname = "easyeffects"
pkgver = "8.3.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "fftw-devel",
    "gsl-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "ladspa-sdk",
    "libbs2b-devel",
    "libebur128-devel",
    "libmysofa-devel",
    "libportal-qt6-devel",
    "libsndfile-devel",
    "lilv-devel",
    "lv2",
    "nlohmann-json",
    "onetbb-devel",
    "pipewire-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtbase-devel",
    "qt6-qtgraphs-devel",
    "rnnoise-devel",
    "soundtouch-devel",
    "speexdsp-devel",
    "turnstile",
    "webrtc-audio-processing-devel",
    "zita-convolver-devel",
]
depends = [
    "kirigami-addons",
    # most plugins are from here and it can crash without them (and at least prints
    # 9 million warnings), so just always pull it
    "lsp-plugins-lv2",
    # ee enforces this qquickstyle by default
    "qqc2-desktop-style",
    "qt6-qtgraphs",
]
pkgdesc = "PipeWire audio plugins"
license = "GPL-3.0-or-later"
url = "https://github.com/wwmm/easyeffects"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d2add92beea6a0e242b2227da5c081c5160b3fe73e681186618dac57207c6037"
tool_flags = {"CXXFLAGS": ["-fexperimental-library"]}


def post_install(self):
    self.install_service(self.files_path / "easyeffects.user")
