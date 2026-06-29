pkgname = "shotwell"
pkgver = "0.32.17"
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
    "gcr3-devel",
    "gexiv2-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
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
sha256 = "0a56684e98817c3103f54a648fe9400427c76a25a7b111457fc1d860c3167672"
