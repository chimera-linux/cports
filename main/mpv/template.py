pkgname = "mpv"
pkgver = "0.40.0"
pkgrel = 4
build_style = "meson"
configure_args = [
    "-Dlibmpv=true",
    "-Dbuild-date=false",
    "-Dtests=true",
    # most of these are autos, force some we really care about
    "-Dcaca=enabled",
    "-Dcdda=enabled",
    "-Dcplugins=enabled",
    "-Ddrm=enabled",
    "-Degl=enabled",
    "-Ddvbin=enabled",
    "-Ddvdnav=enabled",
    "-Dgl=enabled",
    "-Djack=enabled",
    "-Dlcms2=enabled",
    "-Dlibarchive=enabled",
    "-Dlibbluray=enabled",
    "-Dmanpage-build=enabled",
    "-Dpipewire=enabled",
    "-Drubberband=enabled",
    "-Dsixel=enabled",
    "-Duchardet=enabled",
    "-Dvapoursynth=enabled",
    "-Dvaapi=enabled",
    "-Dvulkan=enabled",
    "-Dwayland=enabled",
    "-Dx11=enabled",
    "-Dxv=enabled",
    "-Dzimg=enabled",
    "-Dzlib=enabled",
    # stuff we don't want
    "-Djavascript=disabled",
    "-Dsdl2=disabled",
    "-Dalsa=disabled",
    "-Dopenal=disabled",
    "-Dopensles=disabled",
    "-Doss-audio=disabled",
    "-Dpulse=disabled",
    "-Dsdl2-audio=disabled",
    # misc
    "-Dlua=lua5.1",
]
hostmakedepends = ["meson", "pkgconf", "python-docutils", "wayland-progs"]
makedepends = [
    "ffmpeg-devel",
    "harfbuzz-devel",
    "lcms2-devel",
    "libarchive-devel",
    "libass-devel",
    "libbluray-devel",
    "libcaca-devel",
    "libcdio-paranoia-devel",
    "libdisplay-info-devel",
    "libdvdnav-devel",
    "libplacebo-devel",
    "libsixel-devel",
    "libva-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxpresent-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "libxv-devel",
    "lua5.1-devel",
    "mesa-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "rubberband-devel",
    "uchardet-devel",
    "util-linux-uuid-devel",
    "vapoursynth-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "zimg-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "Video player based on mplayer2"
license = "GPL-2.0-or-later"
url = "https://mpv.io"
source = f"https://github.com/mpv-player/mpv/archive/v{pkgver}.tar.gz"
sha256 = "10a0f4654f62140a6dd4d380dcf0bbdbdcf6e697556863dc499c296182f081a3"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x100000"]}
# FIXME: int causes haruna to crash when started up with some video files
hardening = ["!int", "vis", "!cfi"]


@subpackage("mpv-libs")
def _(self):
    return self.default_libs()


@subpackage("mpv-devel")
def _(self):
    return self.default_devel()
