pkgname = "easyeffects"
pkgver = "7.1.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-libcpp-workarounds=true"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "appstream-glib-devel",
    "fftw-devel",
    "fmt-devel",
    "glib-devel",
    "gsl-devel",
    "gtk4-devel",
    "ladspa-sdk",
    "libadwaita-devel",
    "libbs2b-devel",
    "libebur128-devel",
    "libsamplerate-devel",
    "libsigc++-devel",
    "libsndfile-devel",
    "lilv-devel",
    "lv2",
    "nlohmann-json",
    "onetbb-devel",
    "pipewire-devel",
    "rnnoise-devel",
    "soundtouch-devel",
    "speexdsp-devel",
    "zita-convolver-devel",
]
pkgdesc = "PipeWire audio plugins"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/wwmm/easyeffects"
source = (
    f"https://github.com/wwmm/easyeffects/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "239681eeaba00e7bef57474ead83dd6d41f681eeb6ec8bc8245e24ecbfc2592c"
# FIXME: cfi
hardening = ["vis"]
