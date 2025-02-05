pkgname = "vlc"
# git because no release of 4 yet (qt6, ffmpeg etc)
pkgver = "3.0.20_git20240928"
pkgrel = 2
_gitrev = "e5fc9cc4be87e0f8c7e06e1cedd7e061a390c6ee"
build_style = "gnu_configure"
configure_args = [
    # TODO: explicitly pick stuff (nicer in meson...)
    "--disable-a52",
    "--enable-merge-ffmpeg",
    "--enable-skins2",
]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "protobuf-protoc",
    "qt6-qtbase",
    "qt6-qttools",
    "spirv-tools",
]
makedepends = [
    "avahi-devel",
    "cairo-devel",
    "chromaprint-devel",
    "dav1d-devel",
    "elogind-devel",
    "ffmpeg-devel",
    "flac-devel",
    "fluidsynth-devel",
    "fontconfig-devel",
    "freetype-devel",
    "fribidi-devel",
    "gnutls-devel",
    "gst-plugins-base-devel",
    "kwindowsystem-devel",
    "libaom-devel",
    "libarchive-devel",
    "libass-devel",
    "libbluray-devel",
    "libcddb-devel",
    "libdrm-devel",
    "libdvdnav-devel",
    "libdvdread-devel",
    "libebur128-devel",
    "libgcrypt-devel",
    "libgme-devel",
    "libidn2-devel",
    "libjpeg-turbo-devel",
    "libmatroska-devel",
    "libmicrodns-devel",
    "libmodplug-devel",
    "libmtp-devel",
    "libnfs-devel",
    "libnotify-devel",
    "libogg-devel",
    "libplacebo-devel",
    "libpng-devel",
    "libpulse-devel",
    "librist-devel",
    "librsvg-devel",
    "libsecret-devel",
    "libssh2-devel",
    "libtheora-devel",
    "libva-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "libxcursor-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxml2-devel",
    "libxpm-devel",
    "lua5.4-devel",
    "mesa-devel",
    "mpg123-devel",
    "ncurses-devel",
    "opus-devel",
    "protobuf-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-private-devel",  # qquickitem_p.h/qtguiglobal_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "rnnoise-devel",
    "samba-client-devel",
    "soxr-devel",
    "speex-devel",
    "speexdsp-devel",
    "srt-devel",
    "taglib-devel",
    "twolame-devel",
    "udev-devel",
    "vulkan-loader-devel",
    "x264-devel",
    "x265-devel",
]
pkgdesc = "Multimedia Player"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.videolan.org"
source = f"https://code.videolan.org/videolan/vlc/-/archive/{_gitrev}.tar.gz"
sha256 = "3d5a0b072d275e5f3e2f8afe58625f6e81ff6acfd35d8c9c16f5e9cef8828622"
# v4l2
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# crashes in test_src_input_decoder
hardening = ["!int"]
exec_wrappers = [
    # put it in path
    ("/usr/lib/qt6/bin/qtpaths6", "qtpaths6"),
]
restricted = "does not work well yet"

# TODO:
# - daemon service ?
# - maybe split plugins a bit
# - fill out missing libs


def post_extract(self):
    with open(f"{self.cwd}/src/revision.txt", "w") as rev:
        rev.write(f"{_gitrev}\n")


@subpackage("vlc-devel")
def _(self):
    # FIXME: maybe shouldn't even be installed?
    return self.default_devel(extra=["usr/lib/vlc/libcompat.a"])


@subpackage("vlc-qt")
def _(self):
    self.subdesc = "Qt frontend"
    self.depends = [self.parent]
    return [
        "usr/bin/qvlc",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
        "usr/lib/vlc/plugins/gui/libqt_plugin.so",
    ]


@subpackage("vlc-libs")
def _(self):
    self.triggers = ["/usr/lib/vlc/plugins"]
    return self.default_libs(extra=["usr/libexec/vlc/vlc-cache-gen"])
