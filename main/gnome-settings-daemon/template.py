pkgname = "gnome-settings-daemon"
pkgver = "48.0"
pkgrel = 1
# temporary: https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/issues/867#note_2397625
_gitrev = "90edb8f76e5acfeda5d17f8dd3e690c752283036"
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-settings-daemon"
# source = f"$(GNOME_SITE)/gnome-settings-daemon/{pkgver[:-2]}/gnome-settings-daemon-{pkgver}.tar.xz"
source = [
    f"{url}/-/archive/{_gitrev}.tar.gz",
    "https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/91f3f41490666a526ed78af744507d7ee1134323.tar.gz",
]
source_paths = [".", "subprojects/gvc"]
sha256 = [
    "45d8d50acfdf6428346baaa9358c0bcec9dbf74b193c1b8ca85a50e667ffa9c0",
    "302d1f97ada58b38168d7ce5d5d1df07fc0813e2700b6c69c6f1d7f705ccca29",
]
tool_flags = {"CFLAGS": ["-UG_DISABLE_ASSERT"]}
# wants xvfb
options = ["!check"]


@subpackage("gnome-settings-daemon-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
