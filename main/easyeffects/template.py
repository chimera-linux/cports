pkgname = "easyeffects"
pkgver = "8.2.9"
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
    "qt6-qtgraphs",
]
pkgdesc = "PipeWire audio plugins"
license = "GPL-3.0-or-later"
url = "https://github.com/wwmm/easyeffects"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "549c14277bfecb0a32a6006fcd04e0395d66e4794ec84eb9f491002dea870a22"
tool_flags = {"CXXFLAGS": ["-fexperimental-library"]}


def post_install(self):
    self.install_service(self.files_path / "easyeffects.user")
