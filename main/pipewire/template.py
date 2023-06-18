pkgname = "pipewire"
pkgver = "0.3.71"
pkgrel = 2
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Db_ndebug=false",
    "-Dvulkan=disabled",
    "-Ddocs=enabled",
    "-Dsdl2=disabled",
    "-Dsystemd=disabled",
    "-Dlibcamera=disabled",
    "-Dlibmysofa=disabled",
    "-Droc=disabled",
    "-Dlv2=enabled",
    "-Dbluez5=enabled",
    "-Dbluez5-codec-lc3plus=disabled",
    "-Dpipewire-jack=enabled",  # jack server
    "-Djack-devel=true",  # jack development files
    "-Dlibjack-path=/usr/lib",
    "-Djack=disabled",  # spa plugin
    "-Dlibv4l2-path=/usr/lib",
    "-Dudevrulesdir=/usr/lib/udev/rules.d",
    "-Dsession-managers=[]",
    "-Drlimits-match=@_pipewire",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext-tiny",
    "python-docutils",
    "doxygen",
    "graphviz",
    "glib-devel",
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
    "openssl-devel",
    "webrtc-audio-processing-0.3-devel",
    "bluez-devel",
    "libfreeaptx-devel",
    "libcanberra-devel",
    "lilv-devel",
]
depends = [
    f"libspa-alsa={pkgver}-r{pkgrel}",
    f"libspa-audioconvert={pkgver}-r{pkgrel}",
    f"libspa-audiomixer={pkgver}-r{pkgrel}",
    f"libspa-control={pkgver}-r{pkgrel}",
    f"libspa-v4l2={pkgver}-r{pkgrel}",
    "virtual:pipewire-session-manager!pipewire-session-manager-none",
    "rtkit",
]
pkgdesc = "Server and user space API to deal with multimedia pipelines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.org"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "070dcf83c514903d603351921c7829014c8d9162c49ae5a043290c920f6a6363"
# FIXME int: e.g. https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/2968
hardening = ["!int"]

system_groups = ["_pipewire"]

if self.profile().endian == "big":
    configure_args += ["-Dbluez5-codec-ldac=disabled"]
else:
    makedepends += ["ldacbt-devel"]


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


for _spa in [
    "alsa",
    "audioconvert",
    "audiomixer",
    "control",
    "v4l2",
    "videoconvert",
    "bluez5",
]:
    _genspa(_spa)


@subpackage("gstreamer-pipewire")
def _gst(self):
    self.pkgdesc = f"{pkgdesc} (gstreamer plugin)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gst-plugins-base"]

    return ["usr/lib/gstreamer-1.0"]


@subpackage("alsa-pipewire")
def _alsa(self):
    self.pkgdesc = f"{pkgdesc} (ALSA client library)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "alsa-lib"]

    return [
        "usr/lib/alsa-lib",
        "usr/share/alsa/alsa.conf.d",
    ]


@subpackage("alsa-pipewire-default")
def _alsadef(self):
    self.pkgdesc = f"{pkgdesc} (use for ALSA by default)"
    self.install_if = [f"alsa-pipewire={pkgver}-r{pkgrel}"]

    def inst():
        self.mkdir(self.destdir / "etc/alsa/conf.d", parents=True)
        self.ln_s(
            "../../../usr/share/alsa/alsa.conf.d/99-pipewire-default.conf",
            self.destdir / "etc/alsa/conf.d/99-pipewire-default.conf",
        )

    return inst


@subpackage("pipewire-session-manager-none")
def _wp(self):
    self.pkgdesc = f"{pkgdesc} (no session manager)"
    self.provides = ["pipewire-session-manager=0"]
    self.build_style = "meta"

    return []
