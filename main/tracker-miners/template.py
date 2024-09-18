pkgname = "tracker-miners"
pkgver = "3.7.3"
pkgrel = 3
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
    "-Dlandlock=enabled",
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
    "poppler-devel",
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
source = (
    f"$(GNOME_SITE)/tracker-miners/{pkgver[:-2]}/tracker-miners-{pkgver}.tar.xz"
)
sha256 = "e74388154b5c197b4b7ee42f0dce8c5fbbddd4d361093ef88d4fb303e33da5fe"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
