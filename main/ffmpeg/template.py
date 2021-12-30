pkgname = "ffmpeg"
pkgver = "4.4.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-shared",
    "--enable-static",
    "--enable-gpl",
    "--enable-version3", # for openssl compat when we have it
    "--enable-runtime-cpudetect",
    "--enable-lto",
    #"--enable-openssl", # only once we have openssl 3
    "--enable-postproc",
    "--enable-libjack",
    "--enable-libpulse",
    "--enable-libx264",
    "--enable-libmodplug",
    "--enable-libtheora",
    "--enable-libvorbis",
    "--enable-libopus",
    "--enable-libfreetype",
    "--enable-libopenjpeg",
    "--enable-libwebp",
    "--enable-libass",
    "--enable-libv4l2",
    "--enable-libxcb",
    "--enable-vaapi",
    "--enable-vdpau",
    "--enable-vulkan",
    "--enable-libdrm",
    "--disable-debug",
    "--disable-stripping",
    "--disable-alsa",
    "--disable-libopencore_amrnb",
    "--disable-libopencore_amrwb",
    # TODOs:
    "--disable-libcelt",
    "--disable-libspeex",
    "--disable-libdav1d",
    "--disable-libvpx",
    "--disable-libaom",
    "--disable-libbs2b",
    "--disable-librtmp",
    "--disable-sndio",
    "--disable-libmp3lame",
    "--disable-libxvid",
    "--disable-libcdio",
    "--disable-libvidstab",
    "--disable-opencl",
    "--disable-libx265",
]
make_cmd = "gmake"
make_install_args = ["install-man"]
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf", "perl", "yasm", "texinfo"]
makedepends = [
    "zlib-devel", "libbz2-devel", "openssl-devel",
    "freetype-devel", "harfbuzz-devel",
    "libxfixes-devel", "libxext-devel", "libxvmc-devel", "libxcb-devel",
    "x264-devel",
    "libtheora-devel", "libvorbis-devel", "opus-devel",
    "libwebp-devel", "openjpeg-devel",
    "libass-devel",
    "libmodplug-devel",
    "libpulse-devel", "pipewire-jack-devel",
    "libva-devel", "libvdpau-devel", "v4l-utils-devel",
    "vulkan-loader", "vulkan-headers",
    "libdrm-devel", "sdl-devel",
    # TODOs:
    #"lame-devel",
    #"celt-devel",
    #"x265-devel",
    #"speex-devel",
    #"sndio-devel", # maybe?
    #"dav1d-devel",
    #"libvpx-devel",
    #"libaom-devel",
    #"ocl-icd-devel",
    #"libbs2b-devel",
    #"librtmp-devel",
    #"xvidcore-devel",
    #"libvidstab-devel",
    #"libcdio-paranoia-devel",
]
depends = [f"ffplay={pkgver}-r{pkgrel}"]
pkgdesc = "Decoding, encoding and streaming software"
maintainer = "q66 <q66@chimera-linux.org>"
# we use --enable-gpl; it enables useful filters
license = "GPL-3.0-or-later"
url = "https://ffmpeg.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "eadbad9e9ab30b25f5520fbfde99fae4a92a1ae3c0257a8d68569a4651e30e02"
# seems to need rpath?
options = ["!check"]

if self.profile().cross:
    _archmap = {
        "aarch64": "aarch64",
        "riscv64": "riscv64",
        "ppc64le": "ppc64",
        "ppc64": "ppc64",
        "x86_64": "x8_64",
    }
    if self.profile().arch not in archmap:
        broken = f"unknown architecture: {self.profile().arch}"

    configure_args += [
        "--enable-cross-compile",
        "--target-os=linux",
        "--arch=" + _archmap.get(self.profile().arch, "unknown"),
        f"--sysroot={self.profile().sysroot}",
    ]

def init_configure(self):
    # host toolchain
    self.configure_args += [
        "--host-cc=" + self.get_tool("CC", target = "host"),
        "--host-ld=" + self.get_tool("CC", target = "host"),
        "--host-cflags=" + self.get_cflags(target = "host", shell = True),
        "--host-ldflags=" + self.get_ldflags(target = "host", shell = True),
    ]
    # target toolchain
    self.configure_args += [
        "--cc=" + self.get_tool("CC"),
        "--cxx=" + self.get_tool("CXX"),
        "--ld=" + self.get_tool("CC"),
        "--as=" + self.get_tool("AS"),
        "--ar=" + self.get_tool("AR"),
        "--nm=" + self.get_tool("NM"),
    ]

def _genlib(lname, ldesc):
    @subpackage(f"lib{lname}")
    def _lib(self):
        self.pkgdesc = f"FFmpeg {ldesc} library"
        return [f"usr/lib/lib{lname}.so.*"]

for lname, ldesc in [
    ("avcodec", "codec"),
    ("avdevice", "device handling"),
    ("avformat", "file format"),
    ("avutil", "utility"),
    ("avfilter", "audio/video filter"),
    ("postproc", "video postprocessing"),
    ("swscale", "video scaling"),
    ("swresample", "video resampling"),
]:
    _genlib(lname, ldesc)

@subpackage("ffmpeg-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/share/ffmpeg/examples",
    ])

@subpackage("ffplay")
def _ffplay(self):
    self.pkgdesc = "Simple video player using FFmpeg and SDL"

    return ["usr/bin/ffplay", "usr/share/man/man1/ffplay*"]
