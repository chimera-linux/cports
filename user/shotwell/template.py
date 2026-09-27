pkgname = "shotwell"
pkgver = "33.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dinstall_apport_hook=false",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gcr-devel",
    "gexiv2-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libgee-devel",
    "libgphoto2-devel",
    "libportal-devel",
    "libraw-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libwebp-devel",
]
pkgdesc = "Digital photo organizer"
license = "CC-BY-SA-3.0 AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/shotwell"
source = f"$(GNOME_SITE)/shotwell/{'.'.join(pkgver.split('.')[:2])}/shotwell-{pkgver}.tar.xz"
sha256 = "79f2fa2bd5df3b18d5301012085222eb9a6e548593f6d5dbcea6d1e8559cb797"
