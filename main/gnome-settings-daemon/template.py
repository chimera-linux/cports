pkgname = "gnome-settings-daemon"
pkgver = "47.2"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    # Unpackaged
    "-Dusb-protection=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    # actually pulseaudio is used, alsa is only used to query hw info
    "alsa-lib-devel",
    "colord-devel",
    "cups-devel",
    "gcr-devel",
    "geoclue-devel",
    "geocode-glib-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libgudev-devel",
    "libgweather-devel",
    "libnotify-devel",
    "libpulse-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxfixes-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "pango-devel",
    "polkit-devel",
    "udev-devel",
    "upower-devel",
    "wayland-devel",
]
checkdepends = [
    "elogind",
    "gnome-session",
    "gnome-shell",
    "hwdata",
    "libnotify",
    "python-dbusmock",
    "python-gobject",
    "python-pycodestyle",
    "udev",
    "umockdev",
]
depends = ["iio-sensor-proxy-meta"]
pkgdesc = "GNOME settings daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-settings-daemon"
source = f"$(GNOME_SITE)/gnome-settings-daemon/{pkgver[:-2]}/gnome-settings-daemon-{pkgver}.tar.xz"
sha256 = "1eb758862e888f55a0869193087f1cfbcc7a1163654e630099ff4342dd3f6a5a"
tool_flags = {"CFLAGS": ["-UG_DISABLE_ASSERT"]}
# wants xvfb
options = ["!check"]


@subpackage("gnome-settings-daemon-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
