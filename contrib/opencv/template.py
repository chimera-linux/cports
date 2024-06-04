pkgname = "opencv"
pkgver = "4.10.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    # rm NDEBUG
    "-DCMAKE_BUILD_TYPE=Release",
    # misc
    "-DCMAKE_CXX_STANDARD=17",
    "-DBUILD_EXAMPLES=OFF",
    "-DBUILD_PERF_TESTS=OFF",
    "-DBUILD_TESTS=OFF",  # disabled below
    "-DEIGEN_INCLUDE_PATH=/usr/include/eigen3",
    "-DINSTALL_C_EXAMPLES=OFF",
    "-DINSTALL_PYTHON_EXAMPLES=OFF",
    "-DOPENCV_GENERATE_PKGCONFIG=ON",
    "-DOPENCV_GENERATE_SETUPVARS=OFF",  # useless /usr/bin env scripts
    "-DOPENCV_SKIP_PYTHON_LOADER=ON",  # to allow using as regular cv2 system install
    "-Wno-dev",
    # features
    "-DBUILD_PROTOBUF=OFF",
    "-DBUILD_opencv_python3=ON",
    "-DOPENCL_INCLUDE_DIR=/usr/include",
    "-DOPENCL_LIBRARY=/usr/lib/libOpenCL.so",
    "-DOPENCV_ENABLE_NONFREE=OFF",
    "-DOPENCV_SKIP_FEATURES2D_DOWNLOADING=ON",
    "-DPROTOBUF_UPDATE_FILES=ON",  # to build against system
    "-DVULKAN_INCLUDE_DIRS=/usr/include",
    "-DVULKAN_LIBRARIES=/usr/lib/libvulkan.so",
    "-DWITH_ADE=OFF",  # requires network fetch
    "-DWITH_FLATBUFFERS=OFF",  # otherwise vendored
    "-DWITH_IPP=OFF",
    "-DWITH_OPENCL=ON",
    "-DWITH_OPENGL=ON",
    "-DWITH_OPENMP=ON",
    "-DWITH_QT=ON",
    "-DWITH_TBB=ON",
    "-DWITH_VA=ON",
    "-DWITH_VA_INTEL=ON",
    "-DWITH_VTK=OFF",
    "-DWITH_VULKAN=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "protoc",
    "python-devel",
    "python-numpy",
]
makedepends = [
    "eigen",
    "ffmpeg-devel",
    "freetype-devel",
    "gflags-devel",
    "gflags-devel-static",  # cmake detection
    "glog-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "harfbuzz-devel",
    "libomp-devel",
    "libva-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "mesa-devel",
    "ocl-icd-devel",
    "onetbb-devel",
    "openblas-devel",
    "openexr-devel",
    "openjpeg-devel",
    "protobuf-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
]
pkgdesc = "Computer vision and machine learning libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://opencv.org"
source = [
    f"https://github.com/opencv/opencv/archive/{pkgver}/opencv-{pkgver}.tar.gz",
    f"https://github.com/opencv/opencv_contrib/archive/{pkgver}/opencv_contrib-{pkgver}.tar.gz",
]
source_paths = [
    ".",
    "extra-modules",
]
sha256 = [
    "b2171af5be6b26f7a06b1229948bbb2bdaa74fcf5cd097e0af6378fce50a6eb9",
    "65597f8fb8dc2b876c1b45b928bbcc5f772ddbaf97539bf1b737623d0604cba1",
]
# insane spam on ppc64le
tool_flags = {"CXXFLAGS": ["-Wno-deprecate-lax-vec-conv-all"]}
# of the few manually ran tests, some fail with sigill
hardening = ["!int"]
# TODO: all testsuites need at least some testdata fetched from somewhere..
options = ["!check", "!cross"]

# all libs in /usr/lib + every contrib module
_libs = [
    "alphamat",
    "aruco",
    "calib3d",
    "ccalib",
    "core",
    "cvv",
    "dnn",
    "features2d",
    "flann",
    "freetype",
    "highgui",
    "imgcodecs",
    "imgproc",
    "ml",
    "objdetect",
    "optflow",
    "photo",
    "plot",
    "quality",
    "reg",
    "rgbd",
    "shape",
    "stereo",
    "stitching",
    "superres",
    "surface_matching",
    "tracking",
    "video",
    "videoio",
    "videostab",
    "xfeatures2d",
    "ximgproc",
    "xobjdetect",
    "xphoto",
]


match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]
    case "x86_64":
        configure_args += [
            # defaults to sse3
            "-DCPU_BASELINE_DISABLE=SSE3",
            "-DCPU_BASELINE_REQUIRE=SSE2",
        ]


def post_extract(self):
    # 'contrib' modules. by default all of them are built (from the repo),
    # so keep just whatever we want
    for d in (
        (self.builddir) / f"{self.wrksrc}" / "extra-modules" / "modules"
    ).iterdir():
        if d.name not in [
            "alphamat",
            "aruco",
            "ccalib",
            "cvv",
            "freetype",
            "optflow",
            "plot",
            "quality",
            "reg",
            "rgbd",
            "shape",
            "stereo",
            "superres",
            "surface_matching",
            "tracking",
            "videostab",
            "xfeatures2d",
            "ximgproc",
            "xobjdetect",
            "xphoto",
        ]:
            self.rm(d, recursive=True)


def init_configure(self):
    self.configure_args += [
        f"-DOPENCV_EXTRA_MODULES_PATH={self.chroot_builddir}/{self.wrksrc}/extra-modules/modules",
    ]


@subpackage("opencv-devel")
def _devel(self):
    return self.default_devel()


@subpackage("opencv-progs")
def _progs(self):
    return self.default_progs()


@subpackage("python-opencv")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (python module)"
    self.depends += ["python-numpy"]

    return ["usr/lib/python*"]


def _gen_libpkg(libname):
    @subpackage(f"opencv-{libname}-libs")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({libname})"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        return [f"usr/lib/libopencv_{libname}.so.*"]


for _lib in _libs:
    _gen_libpkg(_lib)
