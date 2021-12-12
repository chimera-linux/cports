pkgname = "pipewire"
pkgver = "0.3.40"
pkgrel = 0
_pms_version = "0.4.1"
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Db_ndebug=false",
    "-Dvulkan=disabled",
    "-Ddocs=disabled", # TODO later
    "-Dsdl2=disabled",
    "-Dsystemd=disabled",
    "-Dlibcamera=disabled",
    "-Droc=disabled",
    "-Dbluez5=disabled", # TODO later
    "-Dbluez5-codec-ldac=disabled", # need ldacbt; little endian only
    "-Dpipewire-jack=enabled", # jack server
    "-Djack-devel=true", # jack development files
    "-Dlibjack-path=/usr/lib",
    "-Djack=disabled", # spa plugin
    "-Dlibv4l2-path=/usr/lib",
    "-Dudevrulesdir=/usr/lib/udev/rules.d",
    "-Dsession-managers=[]",
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
    "alsa-lib-devel",
    "libpulse-devel",
    "fdk-aac-devel",
    "v4l-utils-devel",
    "avahi-devel",
    "webrtc-audio-processing-devel",
    #"libbluetooth-devel", TODO later
    #"libfreeaptx-devel", TODO later
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
source = [f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"]
sha256 = ["a2c8176d757a2ac6db445c61a50802ff1c26f49f5a28174f5eb0278609a887cf"]

system_users = ["_pipewire"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "pipewire.user")
    self.install_service(self.files_path / "pipewire-pulse.user")

@subpackage("libpipewire")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return [
        "usr/lib/libpipewire-*.so.*",
        "usr/lib/pipewire-*/*.so",
    ]

@subpackage("pipewire-jack-devel")
def _jack_devel(self):
    self.pkgdesc = f"{pkgdesc} (JACK development files)"
    self.provides = [f"jack-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/include/jack",
        "usr/lib/pkgconfig/jack.pc",
        "usr/lib/libjack*.so",
    ]

@subpackage("pipewire-jack")
def _jack(self):
    self.pkgdesc = f"{pkgdesc} (JACK support)"
    self.provides = [f"jack={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/pw-jack",
        "usr/lib/libjack*",
        "usr/share/pipewire/jack.conf",
        "usr/share/man/man1/pw-jack.1",
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
    #"bluez5", disabled for now
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

@subpackage("pipewire-doc", False) # TODO later
def _doc(self):
    return self.default_doc()
