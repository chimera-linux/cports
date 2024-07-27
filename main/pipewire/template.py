pkgname = "pipewire"
pkgver = "1.2.1"
pkgrel = 2
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddocs=enabled",
    "-Dman=enabled",
    "-Dsdl2=disabled",  # examples
    "-Dsystemd=disabled",
    "-Dlibffado=disabled",
    "-Droc=disabled",  # TODO
    "-Dselinux=disabled",
    "-Dsnap=disabled",
    "-Dbluez5-codec-lc3plus=disabled",
    "-Djack=disabled",  # spa plugin (to be a jackd client)
    "-Djack-devel=true",  # jack development files (we don't ship jackd)
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
    self.with_pkgver("libspa-aec"),
    self.with_pkgver("libspa-alsa"),
    self.with_pkgver("libspa-audioconvert"),
    self.with_pkgver("libspa-audiomixer"),
    self.with_pkgver("libspa-audiotestsrc"),
    self.with_pkgver("libspa-avb"),
    self.with_pkgver("libspa-control"),
    self.with_pkgver("libspa-support"),
    self.with_pkgver("libspa-v4l2"),
    self.with_pkgver("libspa-videoconvert"),
    self.with_pkgver("libspa-videotestsrc"),
]
pkgdesc = "Server and user space API to deal with multimedia pipelines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.org"
source = f"https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/{pkgver}/pipewire-{pkgver}.tar.gz"
sha256 = "ee26d1e906a930b283d759628de978dc2514522d68f9566f89b1497b2b534f76"

if self.profile().endian == "big":
    configure_args += [
        "-Dbluez5-codec-ldac=disabled",
        "-Decho-cancel-webrtc=disabled",
    ]
else:
    makedepends += ["ldacbt-devel", "webrtc-audio-processing-devel"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "pipewire.conf")
    self.install_service(self.files_path / "pipewire.user", enable=True)
    self.install_service(self.files_path / "pipewire-pulse.user", enable=True)


@subpackage("pipewire-bluetooth")
def _bluez(self):
    self.subdesc = "Bluetooth support"
    self.depends += [self.parent, "bluez"]
    self.install_if = [self.parent, "bluez"]
    self.provides = [self.with_pkgver("libspa-bluez5")]

    return ["usr/lib/spa-0.2/bluez5"]


@subpackage("pipewire-libs")
def _lib(self):
    self.subdesc = "runtime library"
    self.provides = [self.with_pkgver("libpipewire")]
    self.replaces = ["libpipewire<1.0.7-r1"]

    return [
        "usr/lib/libpipewire-*.so.*",
        "usr/lib/pipewire-*/*.so",
        "usr/lib/spa-0.2",
        "usr/share/pipewire/client*",
    ]


@subpackage("pipewire-jack-devel")
def _jack_devel(self):
    self.subdesc = "JACK development files"
    self.provides = [self.with_pkgver("jack-devel")]

    return [
        "usr/include/jack",
        "usr/lib/pkgconfig/jack.pc",
        "usr/lib/libjack*.so",
    ]


@subpackage("pipewire-jack")
def _jack(self):
    self.subdesc = "JACK support"
    self.provides = [self.with_pkgver("jack")]

    return [
        "usr/bin/pw-jack",
        "usr/lib/libjack*",
        "usr/share/pipewire/jack.conf",
        "usr/share/man/man1/pw-jack.1",
    ]


@subpackage("pipewire-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gstreamer-pipewire")
def _gst(self):
    self.subdesc = "gstreamer plugin"
    self.install_if = [self.parent, "gst-plugins-base"]

    return ["usr/lib/gstreamer-1.0"]


@subpackage("alsa-pipewire")
def _alsa(self):
    self.subdesc = "ALSA client library"
    self.install_if = [self.parent, "alsa-lib"]

    return [
        "usr/lib/alsa-lib",
        "usr/share/alsa/alsa.conf.d",
    ]


@subpackage("alsa-pipewire-default")
def _alsadef(self):
    self.subdesc = "use for ALSA by default"
    self.install_if = [self.with_pkgver("alsa-pipewire")]

    return [
        "@etc/alsa/conf.d/99-pipewire-default.conf=>../../../usr/share/alsa/alsa.conf.d/99-pipewire-default.conf"
    ]


@subpackage("pipewire-session-manager-none")
def _wp(self):
    self.subdesc = "no session manager"
    self.provides = ["pipewire-session-manager=0"]
    self.options = ["empty"]

    return []
