pkgname = "feedbackd-device-themes"
pkgver = "0.8.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "vala",
]
makedepends = [
    "json-glib-devel",
]
pkgdesc = "Feedbackd themes for different devices"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/agx/feedbackd-device-themes"
source = f"https://sources.phosh.mobi/releases/feedbackd-device-themes/feedbackd-device-themes-{pkgver}.tar.xz"
sha256 = "73daa199b80ec40ea6f5468e9d3c2948f91da35f6e5d2b52017201131ffe0a5d"
