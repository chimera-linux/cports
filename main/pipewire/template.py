pkgname = "pipewire"
pkgver = "1.0.5"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddocs=enabled",
    "-Dman=enabled",
    "-Dvulkan=disabled",
    "-Dsdl2=disabled",
    "-Dsystemd=disabled",
    "-Dlibcamera=enabled",
    "-Dlibffado=disabled",
    "-Droc=disabled",
    "-Dselinux=disabled",
    "-Dbluez5-codec-lc3plus=disabled",
    "-Djack=disabled",  # spa plugin
    "-Dpipewire-jack=enabled",  # jack server
    "-Djack-devel=true",  # jack development files
    "-Dlibjack-path=/usr/lib",
    "-Dlibv4l2-path=/usr/lib",
    "-Dudevrulesdir=/usr/lib/udev/rules.d",
    "-Dsession-managers=[]",
    "-Drlimits-match=@_pipewire",
]
hostmakedepends = [
    "bash",
    "doxygen",
    "gettext",
    "glib-devel",
    "graphviz",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "alsa-lib-devel",
    "avahi-devel",
    "bluez-devel",
    "fdk-aac-devel",
    "gst-plugins-base-devel",
    "libcamera-devel",
    "libcanberra-devel",
    "libedit-readline-devel",
    "libfreeaptx-devel",
    "liblc3-devel",
    "libmysofa-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "libusb-devel",
    "libva-devel",
    "lilv-devel",
    "ncurses-devel",
    "openssl-devel",
    "sbc-devel",
    "v4l-utils-devel",
]
depends = [
    "virtual:pipewire-session-manager!pipewire-session-manager-none",
    "rtkit",
]
provides = [
    f"libspa-aec={pkgver}-r{pkgrel}",
    f"libspa-alsa={pkgver}-r{pkgrel}",
    f"libspa-audioconvert={pkgver}-r{pkgrel}",
    f"libspa-audiomixer={pkgver}-r{pkgrel}",
    f"libspa-audiotestsrc={pkgver}-r{pkgrel}",
    f"libspa-avb={pkgver}-r{pkgrel}",
    f"libspa-control={pkgver}-r{pkgrel}",
    f"libspa-support={pkgver}-r{pkgrel}",
    f"libspa-v4l2={pkgver}-r{pkgrel}",
    f"libspa-videoconvert={pkgver}-r{pkgrel}",
    f"libspa-videotestsrc={pkgver}-r{pkgrel}",
]
pkgdesc = "Server and user space API to deal with multimedia pipelines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.org"
source = f"https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c5a5de26d684a1a84060ad7b6131654fb2835e03fccad85059be92f8e3ffe993"
# FIXME int: e.g. https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/2968
hardening = ["!int"]

if self.profile().endian == "big":
    configure_args += [
        "-Dbluez5-codec-ldac=disabled",
        "-Decho-cancel-webrtc=disabled",
    ]
else:
    makedepends += ["ldacbt-devel", "webrtc-audio-processing-devel"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(self.files_path / "pipewire.conf", "usr/lib/sysusers.d")
    self.install_service(self.files_path / "pipewire.user", enable=True)
    self.install_service(self.files_path / "pipewire-pulse.user", enable=True)


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


@subpackage("pipewire-bluetooth")
def _bluez(self):
    self.pkgdesc = f"{pkgdesc} (Bluetooth support)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "bluez"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "bluez"]
    self.provides = [f"libspa-bluez5={pkgver}-r{pkgrel}"]

    return ["usr/lib/spa-0.2/bluez5"]


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

    return [
        "@etc/alsa/conf.d/99-pipewire-default.conf=>../../../usr/share/alsa/alsa.conf.d/99-pipewire-default.conf"
    ]


@subpackage("pipewire-session-manager-none")
def _wp(self):
    self.pkgdesc = f"{pkgdesc} (no session manager)"
    self.provides = ["pipewire-session-manager=0"]
    self.options = ["empty"]

    return []
