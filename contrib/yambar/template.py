pkgname = "yambar"
pkgver = "1.11.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dplugin-alsa=enabled",
    "-Dplugin-backlight=enabled",
    "-Dplugin-battery=enabled",
    "-Dplugin-clock=enabled",
    "-Dplugin-cpu=enabled",
    "-Dplugin-disk-io=enabled",
    "-Dplugin-dwl=enabled",
    "-Dplugin-foreign-toplevel=enabled",
    "-Dplugin-mem=enabled",
    "-Dplugin-mpd=enabled",
    "-Dplugin-i3=enabled",
    "-Dplugin-label=enabled",
    "-Dplugin-network=enabled",
    "-Dplugin-pipewire=enabled",
    "-Dplugin-pulse=enabled",
    "-Dplugin-removables=enabled",
    "-Dplugin-river=enabled",
    "-Dplugin-script=enabled",
    "-Dplugin-sway-xkb=enabled",
    "-Dplugin-xkb=enabled",
    "-Dplugin-xwindow=enabled",
]
hostmakedepends = [
    "bison",
    "flex",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "alsa-lib-devel",
    "fcft-devel",
    "json-c-devel",
    "libinput-devel",
    "libmpdclient-devel",
    "libpulse-devel",
    "libxcb-devel",
    "libyaml-devel",
    "pipewire-devel",
    "pixman-devel",
    "tllist",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Modular status panel for X11 and Wayland"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "MIT"
url = "https://codeberg.org/dnkl/yambar"
source = f"{url}/releases/download/{pkgver}/yambar-{pkgver}.tar.gz"
sha256 = "9859ef16ba16069c3442283d76607712c0b7bc602b6fadf41b2c3d97a754d5f9"


def post_install(self):
    self.install_license("LICENSE")
