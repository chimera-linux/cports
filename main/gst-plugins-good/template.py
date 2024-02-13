pkgname = "gst-plugins-good"
pkgver = "1.22.10"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-feature=enabled",
    "-Ddefault_library=shared",
    "-Dglib-asserts=disabled",
    "-Dglib-checks=disabled",
    "-Dgobject-cast-checks=disabled",
    "-Dexamples=disabled",
    "-Ddoc=disabled",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
    "-Ddirectsound=disabled",
    "-Dosxaudio=disabled",
    "-Dosxvideo=disabled",
    "-Doss=disabled",
    "-Doss4=disabled",
    "-Dwaveform=disabled",
    "-Drpicamsrc=disabled",  # proprietary
    "-Dspeex=disabled",  # obsolete, replaced by opus
    "-Dximagesrc=disabled",  # maybe? probably obsolete
    "-Daalib=disabled",  # old and obsolete
    "-Ddv=disabled",  # maybe?
    "-Ddv1394=disabled",  # maybe?
    "-Dqt5=disabled",  # no qt5 in main, maybe package separately?
    "-Dqt6=disabled",  # ditto
    "-Dshout2=disabled",  # libshout needs speex which we don't package
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "orc",
    "nasm",
]
makedepends = [
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "libpng-devel",
    "gtk+3-devel",
    "gdk-pixbuf-devel",
    "bzip2-devel",
    "libxml2-devel",
    "libgudev-devel",
    "v4l-utils-devel",
    "libcaca-devel",
    "pipewire-jack-devel",
    "wavpack-devel",
    "taglib-devel",
    "libvpx-devel",
    "flac-devel",
    "mpg123-devel",
    "lame-devel",
    "twolame-devel",
    "libpulse-devel",
    "orc-devel",
    "libsoup-devel",
]
depends = ["libsoup"]  # dynamically loaded
checkdepends = ["pipewire"]
depends = [f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer good plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f748feae922cad62f20102a84ade8f42b78e1e44a34866aa3ea766f9172e1c7f"
# FIXME int (extra tests fail, look for SIGILL)
hardening = ["!int"]
# 4 out of 105 tests currently fail (qtmux, splitmux, pipelines_tagschecking)
options = ["!check"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
