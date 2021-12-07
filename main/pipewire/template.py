pkgname = "pipewire"
pkgver = "0.3.40"
pkgrel = 0
_pms_version = "0.4.1"
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Db_ndebug=false",
    "-Dvulkan=enabled",
    "-Ddocs=disabled", # TODO later
    "-Dsdl2=disabled",
    "-Dsystemd=disabled",
    "-Dlibcamera=disabled",
    "-Droc=disabled",
    "-Dbluez5=disabled", # TODO later
    "-Dbluez5-codec-ldac=disabled", # need ldacbt; little endian only
    "-Dpipewire-jack=disabled", # TODO later
    "-Djack=disabled", # TODO later
    "-Djack-devel=false",
    "-Dudevrulesdir=/usr/lib/udev/rules.d",
    "-Dmedia-session:systemd=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "python-docutils",
    #"doxygen", "graphviz", TODO later
]
makedepends = [
    "gst-plugins-base-devel",
    "sbc-devel",
    "libva-devel",
    "libusb-devel",
    "libsndfile-devel",
    "libedit-devel",
    "ncurses-devel",
    "vulkan-headers",
    "vulkan-loader",
    "alsa-lib-devel",
    "libpulse-devel",
    "fdk-aac-devel",
    "v4l-utils-devel",
    "avahi-devel",
    "webrtc-audio-processing-devel",
    #"libbluetooth-devel", TODO later
    #"libfreeaptx-devel", TODO later
    #"jack-devel", TODO later
]
depends = [
    f"libspa-alsa={pkgver}-r{pkgrel}",
    f"libspa-audioconvert={pkgver}-r{pkgrel}",
    f"libspa-audiomixer={pkgver}-r{pkgrel}",
    f"libspa-control={pkgver}-r{pkgrel}",
    f"libspa-v4l2={pkgver}-r{pkgrel}",
]
pkgdesc = "Server and user space API to deal with multimedia pipelines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.org"
source = [
    f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"https://gitlab.freedesktop.org/{pkgname}/media-session/-/archive/{_pms_version}/media-session-{_pms_version}.tar.gz",
]
sha256 = [
    "a2c8176d757a2ac6db445c61a50802ff1c26f49f5a28174f5eb0278609a887cf",
    "119c9216070b54018217552c7924f9888da270c3c4647c5e2b85ffa6b1574975",
]

system_users = ["_pipewire"]

def post_extract(self):
    # pipewire itself
    for f in (self.cwd / f"{pkgname}-{pkgver}").iterdir():
        self.mv(f, self.cwd)
    # media-session
    self.mv(f"media-session-{_pms_version}", "subprojects/media-session")

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libpipewire")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return [
        "usr/lib/libpipewire-*.so.*",
        "usr/lib/pipewire-*/*.so",
    ]

@subpackage("pipewire-devel")
def _devel(self):
    return self.default_devel()

def _genspa(spa):
    @subpackage(f"libspa-{spa}")
    def _spa(self):
        self.pkgdesc = f"{pkgdesc} ({spa} plugins)"

        return [f"usr/lib/spa-*/{spa}"]

for spa in [
    "alsa", "audioconvert", "audiomixer", "control", "v4l2", "videoconvert",
    "vulkan",
    #"bluez5", disabled for now
    #"jack",   disabled for now
]:
    _genspa(spa)

@subpackage("gstreamer-pipewire")
def _gst(self):
    self.pkgdesc = f"{pkgdesc} (gstreamer plugin)"

    return ["usr/lib/gstreamer-1.0"]

@subpackage("alsa-pipewire")
def _alsa(self):
    self.pkgdesc = f"{pkgdesc} (ALSA client library)"

    return [
        "usr/lib/alsa-lib",
        "usr/share/alsa/alsa.conf.d",
    ]

@subpackage("libjack-pipewire", False) # disabled for now
def _jack(self):
    self.pkgdesc = f"{pkgdesc} (JACK client library)"

    return [
        "usr/bin/pw-jack",
        "usr/lib/pipewire-*/jack",
        "usr/share/man/man1/pw-jack.1",
    ]

@subpackage("pipewire-doc", False) # TODO later
def _doc(self):
    return self.default_doc()
