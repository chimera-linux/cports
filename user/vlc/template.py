pkgname = "vlc"
pkgver = "3.0.24"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-a52",
    "--disable-alsa",
    "--disable-dca",
    "--disable-dvbpsi",
    "--disable-freerdp",  # not compatible with freerdp 3
    "--disable-gme",
    "--disable-libmpeg2",
    "--disable-libplacebo",  # not compatible with libplacebo 7
    "--disable-live555",
    "--disable-mad",
    "--disable-static",
    "--disable-upnp",
    "--disable-vdpau",
    "--enable-bluray",
    "--enable-chromaprint",
    "--enable-chromecast",
    "--enable-dav1d",
    "--enable-dvdnav",
    "--enable-dvdread",
    "--enable-faad",
    "--enable-flac",
    "--enable-fluidsynth",
    "--enable-fontconfig",
    "--enable-freetype",
    "--enable-fribidi",
    "--enable-gnutls",
    "--enable-gst-decode",
    "--enable-harfbuzz",
    "--enable-jack",
    "--enable-libass",
    "--enable-libgcrypt",
    "--enable-libva",
    "--enable-libxml2",
    "--enable-lua",
    "--enable-matroska",
    "--enable-merge-ffmpeg",
    "--enable-microdns",
    "--enable-mod",
    "--enable-mtp",
    "--enable-ncurses",
    "--enable-nfs",
    "--enable-notify",
    "--enable-ogg",
    "--enable-opus",
    "--enable-pulse",
    "--enable-qt",
    "--enable-librist",
    "--enable-samplerate",
    "--enable-secret",
    "--enable-skins2",
    "--enable-smbclient",
    "--enable-sout",
    "--enable-soxr",
    "--enable-speex",
    "--enable-srt",
    "--enable-svg",
    "--enable-taglib",
    "--enable-theora",
    "--enable-twolame",
    "--enable-udev",
    "--enable-v4l2",
    "--enable-vpx",
    "--enable-wayland",
    "--enable-x264",
    "--enable-x265",
]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./bootstrap"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gettext-devel",
    "libtool",  # slibtool fails to find -lvlc
    "lua5.1",
    "pkgconf",
    "protobuf-protoc",
    "qt6-qtbase",
]
makedepends = [
    "avahi-devel",
    "chromaprint-devel",
    "dav1d-devel",
    "dbus-devel",
    "faad2-devel",
    "ffmpeg-devel",
    "flac-devel",
    "fluidsynth-devel",
    "fontconfig-devel",
    "freerdp-devel",
    "freetype-devel",
    "fribidi-devel",
    "gnutls-devel",
    "gst-plugins-base-devel",
    "harfbuzz-devel",
    "libass-devel",
    "libbluray-devel",
    "libcdio-devel",
    "libdvdnav-devel",
    "libdvdread-devel",
    "libgcrypt-devel",
    "libmatroska-devel",
    "libmicrodns-devel",
    "libmodplug-devel",
    "libmtp-devel",
    "libnfs-devel",
    "libnotify-devel",
    "libogg-devel",
    "libplacebo-devel",
    "libpulse-devel",
    "librist-devel",
    "librsvg-devel",
    "libsamplerate-devel",
    "libsecret-devel",
    "libtheora-devel",
    "libva-devel",
    "libvpx-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxinerama-devel",
    "libxml2-devel",
    "libxpm-devel",
    "linux-headers",
    "lua5.1-devel",
    "mesa-devel",
    "minizip-devel",
    "ncurses-devel",
    "opus-devel",
    "pipewire-jack-devel",
    "protobuf-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "samba-client-devel",
    "soxr-devel",
    "speex-devel",
    "speexdsp-devel",
    "srt-devel",
    "taglib-devel",
    "twolame-devel",
    "udev-devel",
    "v4l-utils-devel",
    "wayland-devel",
    "wayland-protocols",
    "x264-devel",
    "x265-devel",
    "xcbproto",
    "xorgproto",
    "zlib-ng-compat-devel",
]
pkgdesc = "Media player program"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.videolan.org/vlc"
source = f"https://get.videolan.org/vlc/{pkgver}/vlc-{pkgver}.tar.xz"
sha256 = "e7cab503d1d7d5849b89d2cf0e1ee60d0ef6d012407791b644b9cfc0cc225fdf"
# silence about fortify
tool_flags = {
    "CFLAGS": ["-Wno-macro-redefined"],
    "CXXFLAGS": ["-Wno-macro-redefined"],
}
# crashes
hardening = ["!int"]
exec_wrappers = [("/usr/bin/luac5.1", "luac")]


def post_install(self):
    self.uninstall("usr/lib/vlc/libcompat.a")
    self.uninstall("usr/lib/vlc/plugins/plugins.dat")


@subpackage("vlc-qt")
def _(self):
    self.subdesc = "Qt GUI"
    self.depends = [self.parent, "hicolor-icon-theme"]
    self.install_if = [self.parent]

    return [
        "usr/bin/qvlc",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
        "usr/lib/vlc/plugins/gui/libqt*",
    ]


@subpackage("vlc-libs")
def _(self):
    self.triggers = ["/usr/lib/vlc/plugins"]

    def _extras():
        self.take("usr/lib/vlc/vlc-cache-gen")
        # take all the plugins except the ui ones
        for p in (self.parent.destdir / "usr/lib/vlc/plugins").iterdir():
            if p.name == "gui":
                continue
            self.take(f"usr/lib/vlc/plugins/{p.name}")

    return self.default_libs(extra=_extras)


@subpackage("vlc-devel")
def _(self):
    return self.default_devel()
