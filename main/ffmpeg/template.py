pkgname = "ffmpeg"
pkgver = "7.0.1"
pkgrel = 1
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
    "--disable-libcelt",
    "--disable-libopencore_amrnb",
    "--disable-libopencore_amrwb",
    "--disable-libspeex",
    "--disable-sndio",
    "--enable-ladspa",
    "--enable-libaom",
    "--enable-libass",
    "--enable-libbluray",
    "--enable-libbs2b",
    "--enable-libcdio",
    "--enable-libdav1d",
    "--enable-libdrm",
    "--enable-libfreetype",
    "--enable-libharfbuzz",
    "--enable-libjack",
    "--enable-libjxl",
    "--enable-libmodplug",
    "--enable-libmp3lame",
    "--enable-libopenjpeg",
    "--enable-libopus",
    "--enable-libplacebo",
    "--enable-libpulse",
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
    "--enable-opencl",
    "--enable-openssl",
    "--enable-postproc",
    "--enable-runtime-cpudetect",
    "--enable-vaapi",
    "--enable-vapoursynth",
    "--enable-vulkan",
]
make_cmd = "gmake"
make_install_args = ["install-man"]
make_check_args = ["-j1"]
hostmakedepends = [
    "gmake",
    "nasm",
    "perl",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "bzip2-devel",
    "dav1d-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "ladspa-sdk",
    "lame-devel",
    "libaom-devel",
    "libass-devel",
    "libbluray-devel",
    "libbs2b-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libdrm-devel",
    "libjxl-devel",
    "libmodplug-devel",
    "libplacebo-devel",
    "libpulse-devel",
    "librtmp-devel",
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
    "ocl-icd-devel",
    "openjpeg-devel",
    "openssl-devel",
    "opus-devel",
    "pipewire-jack-devel",
    "rubberband-devel",
    "sdl-devel",
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
    "zlib-devel",
]
depends = [f"ffplay={pkgver}-r{pkgrel}"]
pkgdesc = "Decoding, encoding and streaming software"
maintainer = "q66 <q66@chimera-linux.org>"
# we use --enable-gpl; it enables useful filters
license = "GPL-3.0-or-later"
url = "https://ffmpeg.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "bce9eeb0f17ef8982390b1f37711a61b4290dc8c2a0c1a37b5857e85bfb0e4ff"
# seems to need rpath?
options = ["!check"]

if self.profile().arch != "riscv64":
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
    @subpackage(f"lib{lname}")
    def _lib(self):
        self.pkgdesc = f"FFmpeg {ldesc} library"
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
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/share/ffmpeg/examples",
        ]
    )


@subpackage("ffplay")
def _ffplay(self):
    self.pkgdesc = "Simple video player using FFmpeg and SDL"

    return ["usr/bin/ffplay", "usr/share/man/man1/ffplay*"]
