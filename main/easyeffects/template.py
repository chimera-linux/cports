pkgname = "easyeffects"
pkgver = "7.2.0"
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
# most plugins are from here and it can crash without them (and at least prints
# 9 million warnings), so just always pull it
depends = ["dinit-dbus", "lsp-plugins-lv2"]
pkgdesc = "PipeWire audio plugins"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/wwmm/easyeffects"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "524dae04e0295b6bf3ac63e475bf61dfb70eaecf0325408746dec3049515992f"


def post_install(self):
    self.install_service("^/easyeffects.user")
