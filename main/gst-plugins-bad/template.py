pkgname = "gst-plugins-bad"
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
    "-Dhls-crypto=openssl",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
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
    "-Dkate=disabled",
    "-Dmediafoundation=disabled",
    "-Dmsdk=disabled",
    "-Dmusepack=disabled",
    "-Dneon=disabled",
    "-Dnvcodec=disabled",
    "-Donnx=disabled",
    "-Dopenexr=enabled",
    "-Dopenh264=disabled",
    "-Dopenmpt=disabled",
    "-Dopenni2=disabled",
    "-Dopensles=disabled",
    "-Dqsv=disabled",
    "-Dsctp=disabled",
    "-Dsmoothstreaming=disabled",
    "-Dsrt=disabled",
    "-Dsvthevcenc=disabled",
    "-Dteletext=disabled",
    "-Dtinyalsa=disabled",
    "-Dvoaacenc=disabled",
    "-Dvoamrwbenc=disabled",
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
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "orc",
    "gobject-introspection",
    "shaderc-progs",
    "wayland-progs",
]
makedepends = [
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "openssl-devel",
    "libaom-devel",
    "libass-devel",
    "bluez-devel",
    "libbs2b-devel",
    "bzip2-devel",
    "pango-devel",
    "cairo-devel",
    "lcms2-devel",
    "libcurl-devel",
    "libssh2-devel",
    "libxml2-devel",
    "fdk-aac-devel",
    "fluidsynth-devel",
    "mesa-devel",
    "libdrm-devel",
    "libde265-devel",
    "libmodplug-devel",
    "openexr-devel",
    "openjpeg-devel",
    "opus-devel",
    "sbc-devel",
    "librsvg-devel",
    "librtmp-devel",
    "libsndfile-devel",
    "libva-devel",
    "vulkan-loader-devel",
    "vulkan-headers",
    "libwebp-devel",
    "libgudev-devel",
    "wayland-devel",
    "wayland-protocols",
    "libxkbcommon-devel",
    "v4l-utils-devel",
    "libusb-devel",
    "libfreeaptx-devel",
    "lilv-devel",
    "ladspa-sdk",
    "lrdf-devel",
    "chromaprint-devel",
    "gtk+3-devel",
    "openal-soft-devel",
    "qrencode-devel",
    "json-glib-devel",
    "libnice-devel",
    "libsrtp-devel",
    "spandsp-devel",
    "soundtouch-devel",
    "libmicrodns-devel",
    "gsm-devel",
    "libgme-devel",
    "linux-headers",
]
depends = [f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer bad plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "dabcd60c762165bb043eba753d599212514c94684e4db9a2e25484cb6508ebbf"
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
def _devel(self):
    self.depends += [f"gst-plugins-base-devel~{pkgver}"]

    return self.default_devel()
