pkgname = "easyeffects"
pkgver = "7.1.9"
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b22a62c7bf51930cafdedbf3afcd93b736f4fed5f4bb21d55dd2190436f80844"
