pkgname = "pipewire"
pkgver = "1.2.7"
pkgrel = 3
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddocs=enabled",
    "-Dman=enabled",
    "-Dlogind-provider=libelogind",
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
    "elogind-devel",
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
    "openssl3-devel",
    "sbc-devel",
    "v4l-utils-devel",
]
depends = [
    "dinit-dbus",
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
sha256 = "e75568ed18bcbe75e9779af57cb9cc256fd7ebfaadc12bb347a0717055d1d3a9"

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
    # move to vendordir
    self.install_dir("usr/share/pam")
    self.rename("etc/security", "usr/share/pam/security", relative=False)


@subpackage("pipewire-bluetooth")
def _(self):
    self.subdesc = "Bluetooth support"
    self.depends += [self.parent, "bluez"]
    self.install_if = [self.parent, "bluez"]
    self.provides = [self.with_pkgver("libspa-bluez5")]

    return ["usr/lib/spa-0.2/bluez5"]


@subpackage("pipewire-libs")
def _(self):
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
def _(self):
    self.subdesc = "JACK development files"
    self.provides = [self.with_pkgver("jack-devel")]

    return [
        "usr/include/jack",
        "usr/lib/pkgconfig/jack.pc",
        "usr/lib/libjack*.so",
    ]


@subpackage("pipewire-jack")
def _(self):
    self.subdesc = "JACK support"
    self.provides = [self.with_pkgver("jack")]

    return [
        "usr/bin/pw-jack",
        "usr/lib/libjack*",
        "usr/share/pipewire/jack.conf",
        "usr/share/man/man1/pw-jack.1",
    ]


@subpackage("pipewire-devel")
def _(self):
    return self.default_devel()


@subpackage("pipewire-gstreamer")
def _(self):
    self.subdesc = "gstreamer plugin"
    self.install_if = [self.parent, "gst-plugins-base"]
    # transitional
    self.provides = [self.with_pkgver("gstreamer-pipewire")]

    return ["usr/lib/gstreamer-1.0"]


@subpackage("pipewire-alsa")
def _(self):
    self.subdesc = "ALSA client library"
    self.install_if = [self.parent, "alsa-lib"]
    # transitional
    self.provides = [self.with_pkgver("alsa-pipewire")]

    return [
        "usr/lib/alsa-lib",
        "usr/share/alsa/alsa.conf.d",
    ]


@subpackage("pipewire-alsa-default")
def _(self):
    self.subdesc = "use for ALSA by default"
    self.install_if = [self.with_pkgver("pipewire-alsa")]
    # transitional
    self.provides = [self.with_pkgver("alsa-pipewire-default")]

    return [
        "@etc/alsa/conf.d/99-pipewire-default.conf=>../../../usr/share/alsa/alsa.conf.d/99-pipewire-default.conf"
    ]


@subpackage("pipewire-session-manager-none")
def _(self):
    self.subdesc = "no session manager"
    self.provides = ["pipewire-session-manager=0"]
    self.options = ["empty"]

    return []
