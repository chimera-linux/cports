pkgname = "tracker-miners"
pkgver = "3.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddefault_library=shared",
    "-Dtracker_core=system", "-Dextract=true", "-Dfunctional_tests=false",
    "-Dman=true", "-Dsystemd_user_services=false",
    # features
    "-Dminer_rss=false", # TODO: libgrss
    "-Dxmp=disabled", # TODO: exempi
    "-Draw=disabled", # TODO: gexiv2
    "-Dcue=disabled", # TODO: libcue
    "-Dgsf=disabled", # TODO: libgsf
    "-Dxps=disabled", # TODO: libgxps
    "-Diso=disabled", # TODO: libosinfo
    "-Diptc=disabled", # TODO: libiptcdata
    "-Dplaylist=disabled", # TODO: totem-pl-parser
    "-Dexif=enabled",
    "-Djpeg=enabled",
    "-Dtiff=enabled",
    "-Dpng=enabled",
    "-Dgif=enabled",
    "-Dpdf=enabled",
    "-Dxml=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "asciidoc", "xsltproc",
]
makedepends = [
    "tracker-devel", "libglib-devel", "dbus-devel", "gstreamer-devel",
    "gst-plugins-base-devel", "icu-devel", "libexif-devel", "libseccomp-devel",
    "libjpeg-turbo-devel", "libpng-devel", "libtiff-devel", "giflib-devel",
    "libxml2-devel", "libpoppler-glib-devel", "upower-devel",
    "networkmanager-devel",
    # FIXMEs:
    #"libcue-devel",
    #"libgsf-devel",
    #"exempi-devel",
    #"libgrss-devel",
    #"libgxps-devel",
    #"libosinfo-devel",
    #"libgexiv2-devel",
    #"libiptcdata-devel",
]
pkgdesc = "Data miners for tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "44369f53e2edef41437406dbeecd477a97f8a9afdd9134832ea45d1ba2aa2c47"
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
