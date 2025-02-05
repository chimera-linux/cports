pkgname = "ffmpeg"
pkgver = "7.1"
pkgrel = 5
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-shared",
    "--enable-static",
    "--enable-gpl",
    "--enable-version3",
    "--disable-debug",
    "--disable-stripping",
    # features
    "--disable-alsa",
    "--disable-indev=oss",
    "--disable-libcelt",
    "--disable-libopencore_amrnb",
    "--disable-libopencore_amrwb",
    "--disable-libspeex",
    "--disable-outdev=oss",
    "--disable-sndio",
    "--enable-ladspa",
    "--enable-lcms2",
    "--enable-libaom",
    "--enable-libass",
    "--enable-libbluray",
    "--enable-libbs2b",
    "--enable-libcdio",
    "--enable-libdav1d",
    "--enable-libdrm",
    "--enable-libdvdnav",
    "--enable-libdvdread",
    "--enable-libfontconfig",
    "--enable-libfreetype",
    "--enable-libfribidi",
    "--enable-libharfbuzz",
    "--enable-libjack",
    "--enable-libjxl",
    "--enable-libmodplug",
    "--enable-libmp3lame",
    "--enable-libopenjpeg",
    "--enable-libopenmpt",
    "--enable-libopus",
    "--enable-libplacebo",
    "--enable-libpulse",
    "--enable-librav1e",
    "--enable-librsvg",
    "--enable-librtmp",
    "--enable-librubberband",
    "--enable-libshaderc",
    "--enable-libsoxr",
    "--enable-libsvtav1",
    "--enable-libtheora",
    "--enable-libv4l2",
    "--enable-libvidstab",
    "--enable-libvorbis",
    "--enable-libvpx",
    "--enable-libwebp",
    "--enable-libx264",
    "--enable-libx265",
    "--enable-libxcb",
    "--enable-libxml2",
    "--enable-libxvid",
    "--enable-libzimg",
    "--enable-lv2",
    "--enable-opencl",
    "--enable-openssl",
    "--enable-postproc",
    "--enable-runtime-cpudetect",
    "--enable-vaapi",
    "--enable-vapoursynth",
    "--enable-vulkan",
]
make_install_args = ["install-man"]
make_check_args = ["-j1"]
hostmakedepends = [
    "nasm",
    "perl",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "dav1d-devel",
    "fontconfig-devel",
    "freetype-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "ladspa-sdk",
    "lame-devel",
    "lcms2-devel",
    "libaom-devel",
    "libass-devel",
    "libbluray-devel",
    "libbs2b-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libdrm-devel",
    "libdvdnav-devel",
    "libdvdread-devel",
    "libjxl-devel",
    "libmodplug-devel",
    "libopenmpt-devel",
    "libplacebo-devel",
    "libpulse-devel",
    "librsvg-devel",
    "libtheora-devel",
    "libva-devel",
    "libvidstab-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "libwebp-devel",
    "libxcb-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxml2-devel",
    "libxvmc-devel",
    "lilv-devel",
    "ocl-icd-devel",
    "openjpeg-devel",
    "openssl3-devel",
    "opus-devel",
    "pipewire-jack-devel",
    "rav1e-devel",
    "rtmpdump-devel",
    "rubberband-devel",
    "sdl2-compat-devel",
    "shaderc-devel",
    "soxr-devel",
    "svt-av1-devel",
    "v4l-utils-devel",
    "vapoursynth-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "x264-devel",
    "x265-devel",
    "xvidcore-devel",
    "zimg-devel",
    "zlib-ng-compat-devel",
]
depends = [self.with_pkgver("ffmpeg-ffplay")]
pkgdesc = "Decoding, encoding and streaming software"
maintainer = "q66 <q66@chimera-linux.org>"
# we use --enable-gpl; it enables useful filters
license = "GPL-3.0-or-later"
url = "https://ffmpeg.org"
source = f"{url}/releases/ffmpeg-{pkgver}.tar.xz"
sha256 = "40973d44970dbc83ef302b0609f2e74982be2d85916dd2ee7472d30678a7abe6"
# some conf checks like for some pthread functions don't detect interfaces
# without it
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# seems to need rpath?
options = ["!check"]

if self.has_lto(force=True):
    configure_args += ["--enable-lto=thin"]

if self.profile().cross:
    _archmap = {
        "aarch64": "aarch64",
        "ppc64le": "ppc64",
        "ppc64": "ppc64",
        "ppc": "ppc",
        "riscv64": "riscv",
        "x86_64": "x86_64",
    }
    if self.profile().arch not in _archmap:
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
        "--host-cc=" + self.get_tool("CC", target="host"),
        "--host-ld=" + self.get_tool("CC", target="host"),
        "--host-cflags=" + self.get_cflags(target="host", shell=True),
        "--host-ldflags=" + self.get_ldflags(target="host", shell=True),
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
    @subpackage(f"ffmpeg-{lname}-libs")
    def _(self):
        self.pkgdesc = f"FFmpeg {ldesc} library"
        # transitional
        self.provides = [self.with_pkgver(f"lib{lname}")]
        return [f"usr/lib/lib{lname}.so.*"]


for _lname, _ldesc in [
    ("avcodec", "codec"),
    ("avdevice", "device handling"),
    ("avformat", "file format"),
    ("avutil", "utility"),
    ("avfilter", "audio/video filter"),
    ("postproc", "video postprocessing"),
    ("swscale", "video scaling"),
    ("swresample", "video resampling"),
]:
    _genlib(_lname, _ldesc)


@subpackage("ffmpeg-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/share/ffmpeg/examples",
        ]
    )


@subpackage("ffmpeg-ffplay")
def _(self):
    self.pkgdesc = "Simple video player using FFmpeg and SDL"
    # transitional
    self.provides = [self.with_pkgver("ffplay")]

    return ["cmd:ffplay"]
