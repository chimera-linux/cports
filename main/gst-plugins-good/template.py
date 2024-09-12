pkgname = "gst-plugins-good"
pkgver = "1.24.7"
pkgrel = 2
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
    "-Daalib=disabled",  # old and obsolete
    "-Damrnb=disabled",
    "-Damrwbdec=disabled",
    "-Ddirectsound=disabled",
    "-Ddv1394=disabled",  # maybe?
    "-Ddv=disabled",  # maybe?
    "-Doss4=disabled",
    "-Doss=disabled",
    "-Dosxaudio=disabled",
    "-Dosxvideo=disabled",
    "-Dqt5=disabled",  # no qt5
    "-Dqt6=disabled",  # in contrib
    "-Drpicamsrc=disabled",  # proprietary
    "-Dshout2=disabled",  # libshout needs speex which we don't package
    "-Dspeex=disabled",  # obsolete, replaced by opus
    "-Dv4l2-libv4l2=disabled",  # uses v4l2 directly, lib not used by default
    "-Dwaveform=disabled",
    "-Dximagesrc=disabled",  # maybe? probably obsolete
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
sha256 = "759acb11e6de8373ff8cbb5e7ab8eb9a38631be81cf24220267b001eb55593c1"
# FIXME int (extra tests fail, look for SIGILL)
# in 1.24.4, pipelines_effectv only
hardening = ["!int"]
