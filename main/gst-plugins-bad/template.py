pkgname = "gst-plugins-bad"
pkgver = "1.24.11"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    "-Dglib-asserts=disabled",
    "-Dglib-checks=disabled",
    "-Dgobject-cast-checks=disabled",
    # disabled below
    "-Dtests=disabled",
    "-Dexamples=disabled",
    "-Ddoc=disabled",
    "-Dhls-crypto=openssl",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
    "-Daja=disabled",
    "-Dopencv=disabled",
    "-Damfcodec=disabled",
    "-Dandroidmedia=disabled",
    "-Dapplemedia=disabled",
    "-Dd3dvideosink=disabled",
    "-Dd3d11=disabled",
    "-Ddirectfb=disabled",
    "-Ddirectshow=disabled",
    "-Ddirectsound=disabled",
    "-Dfaac=disabled",
    "-Dfbdev=disabled",
    "-Dmediafoundation=disabled",
    "-Dmsdk=disabled",
    "-Dmusepack=disabled",
    "-Dneon=disabled",
    "-Dnvcodec=disabled",
    "-Donnx=disabled",
    "-Dopenh264=disabled",
    "-Dopenmpt=disabled",
    "-Dopenni2=disabled",
    "-Dopensles=disabled",
    "-Dqsv=disabled",
    "-Dsmoothstreaming=disabled",
    "-Dsrt=disabled",
    "-Dsvthevcenc=disabled",
    "-Dteletext=disabled",
    "-Dtinyalsa=disabled",
    "-Dvoaacenc=disabled",
    "-Dvoamrwbenc=disabled",
    "-Dqt6d3d11=disabled",
    "-Dwasapi=disabled",
    "-Dwasapi2=disabled",
    "-Dwildmidi=disabled",
    "-Dwinks=disabled",
    "-Dwinscreencap=disabled",
    "-Dwpe=disabled",
    "-Dmagicleap=disabled",
    "-Davtp=disabled",
    "-Ddc1394=disabled",  # maybe?
    "-Ddts=disabled",  # GPL
    "-Dfaad=disabled",  # GPL
    "-Dgs=disabled",  # does anybody need this?
    "-Diqa=disabled",  # AGPL
    "-Dmpeg2enc=disabled",  # GPL
    "-Dmplex=disabled",  # GPL
    "-Dresindvd=disabled",  # GPL
    "-Dx265=disabled",  # GPL
    "-Dzbar=disabled",  # maybe?
    "-Dzxing=disabled",  # maybe?
    "-Dflite=disabled",  # not packaged, fails with make 4.4
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "orc",
    "pkgconf",
    "shaderc-progs",
    "wayland-progs",
]
makedepends = [
    "bluez-devel",
    "bzip2-devel",
    "cairo-devel",
    "chromaprint-devel",
    "fdk-aac-devel",
    "fluidsynth-devel",
    "gsm-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "ladspa-sdk",
    "lcms2-devel",
    "libaom-devel",
    "libass-devel",
    "libbs2b-devel",
    "curl-devel",
    "libde265-devel",
    "libdrm-devel",
    "libfreeaptx-devel",
    "libgme-devel",
    "libgudev-devel",
    "liblc3-devel",
    "libmicrodns-devel",
    "libmodplug-devel",
    "libnice-devel",
    "librsvg-devel",
    "librtmp-devel",
    "libsndfile-devel",
    "libsrtp-devel",
    "libssh2-devel",
    "libusb-devel",
    "libva-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "lilv-devel",
    "linux-headers",
    "lrdf-devel",
    "mesa-devel",
    "openal-soft-devel",
    "openexr-devel",
    "openjpeg-devel",
    "openssl-devel",
    "opus-devel",
    "pango-devel",
    "qrencode-devel",
    "sbc-devel",
    "soundtouch-devel",
    "spandsp-devel",
    "svt-av1-devel",
    "usrsctp-devel",
    "v4l-utils-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer bad plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-bad/gst-plugins-bad-{pkgver}.tar.xz"
sha256 = "9126c2b7053a5f059db958f43c6a5230d2e843ff9adff8c8c2477ea2457e3315"
# FIXME int
hardening = ["!int"]
# TODO: a few fails, debug later
options = ["!check", "!cross"]

if self.profile().endian == "big":
    configure_args += [
        "-Dldac=disabled",
        "-Disac=disabled",
        "-Dwebrtcdsp=disabled",
    ]
else:
    makedepends += ["ldacbt-devel", "webrtc-audio-processing-devel"]


@subpackage("gst-plugins-bad-devel")
def _(self):
    self.depends += [f"gst-plugins-base-devel~{pkgver}"]

    return self.default_devel()
