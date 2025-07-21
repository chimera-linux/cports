pkgname = "localsearch"
pkgver = "3.9.0"
pkgrel = 2
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddefault_library=shared",
    "-Dextract=true",
    "-Dfunctional_tests=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    # features
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
    "asciidoc",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "exempi-devel",
    "ffmpeg-devel",
    "gexiv2-devel",
    "giflib-devel",
    "glib-devel",
    "icu-devel",
    "libcue-devel",
    "libexif-devel",
    "libgsf-devel",
    "libgudev-devel",
    "libgxps-devel",
    "libiptcdata-devel",
    "libjpeg-turbo-devel",
    "libosinfo-devel",
    "libpng-devel",
    "libseccomp-devel",
    "libtiff-devel",
    "libxml2-devel",
    "linux-headers",
    "networkmanager-devel",
    "poppler-devel",
    "tinysparql-devel",
    "totem-pl-parser-devel",
    "upower-devel",
]
provides = [self.with_pkgver("tracker-miners")]
pkgdesc = "Data miners for tinysparql"
license = "GPL-2.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/localsearch/{pkgver[:-2]}/localsearch-{pkgver}.tar.xz"
sha256 = "d42f408dc3fb28fe54f5a9abbf5f1decf5818db9c2e9ec51c09464bdfd0c14b9"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
