pkgname = "gst-plugins-good"
pkgver = "1.24.4"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # misc
    "-Ddoc=disabled",
    "-Dexamples=disabled",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
    "-Damrnb=disabled",
    "-Damrwbdec=disabled",
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
    "-Dqt5=disabled",  # no qt5
    "-Dqt6=disabled",  # in contrib
    "-Dshout2=disabled",  # libshout needs speex which we don't package
]
make_check_args = ["--timeout-multiplier=5"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "nasm",
    "orc",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "flac-devel",
    "gdk-pixbuf-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "lame-devel",
    "libcaca-devel",
    "libgudev-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsoup-devel",
    "libvpx-devel",
    "libxml2-devel",
    "mpg123-devel",
    "orc-devel",
    "pipewire-jack-devel",
    "taglib-devel",
    "twolame-devel",
    "v4l-utils-devel",
    "wavpack-devel",
]
depends = ["libsoup"]  # dynamically loaded
checkdepends = ["xwayland-run"]
depends = [f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer good plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-good/gst-plugins-good-{pkgver}.tar.xz"
sha256 = "023096d661cf58cde3e0dcdbf56897bf588830232358c305f3e15fd63e116626"
# sys/v4l2/gstv4l2object.c v4l2object->ioctl = v4l2_ioctl;
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# FIXME int (extra tests fail, look for SIGILL)
# in 1.24.4, pipelines_effectv only
hardening = ["!int"]
