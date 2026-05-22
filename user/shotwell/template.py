pkgname = "shotwell"
pkgver = "0.32.15"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
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
sha256 = "ac10260f382e1a3193bbb0dac8143163f1ca35546fa76133d542e390af742f3a"
