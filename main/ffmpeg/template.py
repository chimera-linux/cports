pkgname = "ffmpeg"
pkgver = "6.1.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-shared",
    "--enable-static",
    "--enable-gpl",
    "--enable-version3",
    "--enable-runtime-cpudetect",
    "--enable-openssl",
    "--enable-librtmp",
    "--enable-postproc",
    "--enable-libjack",
    "--enable-libpulse",
    "--enable-libxvid",
    "--enable-libx264",
    "--enable-libx265",
    "--enable-libvpx",
    "--enable-libaom",
    "--enable-libdav1d",
    "--enable-libvidstab",
    "--enable-libmp3lame",
    "--enable-libsvtav1",
    "--enable-libmodplug",
    "--enable-libbs2b",
    "--enable-libtheora",
    "--enable-libvorbis",
    "--enable-libsoxr",
    "--enable-libopus",
    "--enable-libcdio",
    "--enable-libbluray",
    "--enable-libfreetype",
    "--enable-libharfbuzz",
    "--enable-libopenjpeg",
    "--enable-libplacebo",
    "--enable-libwebp",
    "--enable-libzimg",
    "--enable-libass",
    "--enable-libv4l2",
    "--enable-libxcb",
    "--enable-librubberband",
    "--enable-libxml2",
    "--enable-opencl",
    "--enable-vaapi",
    "--enable-vapoursynth",
    "--enable-vulkan",
    "--enable-libdrm",
    "--disable-debug",
    "--disable-stripping",
    "--disable-alsa",
    "--disable-sndio",
    "--disable-libopencore_amrnb",
    "--disable-libopencore_amrwb",
    "--disable-libcelt",
    "--disable-libspeex",
]
make_cmd = "gmake"
make_install_args = ["install-man"]
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf", "perl", "nasm", "texinfo"]
makedepends = [
    "zlib-devel",
    "bzip2-devel",
    "openssl-devel",
    "librtmp-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "zimg-devel",
    "libxfixes-devel",
    "libxext-devel",
    "libxvmc-devel",
    "libxcb-devel",
    "x264-devel",
    "x265-devel",
    "xvidcore-devel",
    "dav1d-devel",
    "libvpx-devel",
    "libaom-devel",
    "libvidstab-devel",
    "libplacebo-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "opus-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "libbluray-devel",
    "libass-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libmodplug-devel",
    "lame-devel",
    "libbs2b-devel",
    "libpulse-devel",
    "pipewire-jack-devel",
    "vapoursynth-devel",
    "libva-devel",
    "v4l-utils-devel",
    "vulkan-loader-devel",
    "vulkan-headers",
    "libdrm-devel",
    "sdl-devel",
    "svt-av1-devel",
    "soxr-devel",
    "rubberband-devel",
    "libxml2-devel",
    "ocl-icd-devel",
]
depends = [f"ffplay={pkgver}-r{pkgrel}"]
pkgdesc = "Decoding, encoding and streaming software"
maintainer = "q66 <q66@chimera-linux.org>"
# we use --enable-gpl; it enables useful filters
license = "GPL-3.0-or-later"
url = "https://ffmpeg.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "8684f4b00f94b85461884c3719382f1261f0d9eb3d59640a1f4ac0873616f968"
# seems to need rpath?
options = ["!check"]

if self.profile().arch != "riscv64":
    configure_args += ["--enable-lto=thin"]
else:
    # asm fails to build
    configure_args += ["--disable-rvv"]

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
