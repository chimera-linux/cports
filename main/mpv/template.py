pkgname = "mpv"
pkgver = "0.34.1"
pkgrel = 0
build_style = "waf"
configure_args = [
    "--confdir=/etc/mpv", "--docdir=/usr/share/examples/mpv",
    "--zshdir=/usr/share/zsh/site-functions", "--enable-libmpv-shared",
    "--enable-cplugins", "--enable-cdda", "--enable-dvbin",
    "--enable-dvdnav", "--enable-libarchive", "--enable-pulse",
    "--enable-jack", "--enable-lcms2", "--enable-lua", "--enable-vdpau",
    "--enable-vulkan", "--enable-shaderc", "--enable-wayland",
    "--enable-x11", "--enable-caca", "--enable-vapoursynth",
    "--enable-zimg",
    "--disable-alsa", "--disable-openal", "--disable-sdl2",
]
hostmakedepends = [
    "pkgconf", "python", "python-docutils", "wayland-progs"
]
makedepends = [
    "libarchive-devel", "lua5.1-devel", "libuuid-devel", "mesa-devel",
    "vulkan-headers", "vulkan-loader", "libplacebo-devel", "shaderc-devel",
    "ffmpeg-devel", "libxv-devel", "libxrandr-devel", "libxinerama-devel",
    "libxscrnsaver-devel", "libxkbcommon-devel", "wayland-devel",
    "wayland-protocols", "libvdpau-devel", "libva-devel", "libpulse-devel",
    "pipewire-jack-devel", "lcms2-devel", "libass-devel", "libbluray-devel",
    "libdvdnav-devel", "libcdio-paranoia-devel", "rubberband-devel",
    "uchardet-devel", "harfbuzz-devel", "libcaca-devel", "zimg-devel",
    "vapoursynth-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "Video player based on mplayer2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://mpv.io"
source = f"https://github.com/mpv-player/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "32ded8c13b6398310fa27767378193dc1db6d78b006b70dbcbd3123a1445e746"
# no test suite
options = ["!check"]

def post_patch(self):
    self.do("python", "bootstrap.py", allow_network = True)

@subpackage("mpv-devel")
def _devel(self):
    return self.default_devel()
