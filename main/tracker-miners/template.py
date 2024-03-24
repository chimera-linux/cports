pkgname = "tracker-miners"
pkgver = "3.7.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddefault_library=shared",
    "-Dtracker_core=system",
    "-Dextract=true",
    "-Dfunctional_tests=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    # features
    "-Dminer_rss=false",  # libgrss hasn't been touched in a while
    "-Dplaylist=enabled",
    "-Dexif=enabled",
    "-Djpeg=enabled",
    "-Dtiff=enabled",
    "-Diptc=enabled",
    "-Draw=enabled",
    "-Dxps=enabled",
    "-Dpng=enabled",
    "-Dgif=enabled",
    "-Dpdf=enabled",
    "-Dxml=enabled",
    "-Dcue=enabled",
    "-Dgsf=enabled",
    "-Diso=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "asciidoc",
    "xsltproc",
]
makedepends = [
    "tracker-devel",
    "glib-devel",
    "dbus-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "icu-devel",
    "libexif-devel",
    "libseccomp-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "giflib-devel",
    "libxml2-devel",
    "libpoppler-glib-devel",
    "upower-devel",
    "exempi-devel",
    "networkmanager-devel",
    "gexiv2-devel",
    "totem-pl-parser-devel",
    "libgxps-devel",
    "libcue-devel",
    "libgsf-devel",
    "libiptcdata-devel",
    "libosinfo-devel",
]
pkgdesc = "Data miners for tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "74e796c1625094a8a2175993c7907281e97ab6e002578e846b8f4ca44e36bf61"
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
