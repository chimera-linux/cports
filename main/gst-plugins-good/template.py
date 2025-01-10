pkgname = "gst-plugins-good"
pkgver = "1.24.11"
pkgrel = 0
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
    "qt6-qtbase",
    "qt6-qttools",
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
    "qt6-qtbase-private-devel",  # qrhi_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
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
sha256 = "94bf3b5118dd4213af66048faac830569cc9a94a8c8e59e8a6d33b315f518462"
# FIXME int (extra tests fail, look for SIGILL)
# in 1.24.4, pipelines_effectv only
hardening = ["!int"]


@subpackage("gst-plugins-good-qt6")
def _(self):
    self.subdesc = "Qt6 plugin"

    return ["usr/lib/gstreamer-1.0/libgstqml*.so"]
