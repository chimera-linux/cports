pkgname = "pavucontrol"
pkgver = "6.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "lynx",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "gtkmm-devel",
    "json-glib-devel",
    "libcanberra-devel",
    "libpulse-devel",
    "libsigc++-devel",
]
pkgdesc = "PulseAudio volume control"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/software/pulseaudio/pavucontrol"
source = f"https://gitlab.freedesktop.org/pulseaudio/pavucontrol/-/archive/v{pkgver}.tar.gz"
sha256 = "b6c40918c0d4767f7cdbc04484adb7bbaacc41020678de6ac80d4b59640b94f8"
