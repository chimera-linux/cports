pkgname = "taisei"
pkgver = "1.4.4"
_koishi = "f899ac2f96051ffbc6cf9aa250f52832f0dfef9b"
_basis_universal = "380ef9389b38ec42506d5728dd05e94ac2f3c301"
_gamecontrollerdb = "18497288979145853f9a60d61c592267de56cd5e"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgamemode=disabled",
    "-Db_ndebug=true",
    "--wrap-mode=nofallback",
    "-Dcpp_rtti=true",
    "-Ddefault_library=static",  # needed for libkoishi
]
makedepends = [
    "cglm",
    "cmake",
    "cryptsetup-devel",
    "freetype-devel",
    "libwebp-devel",
    "libzip-devel",
    "mesa-opencl",
    "meson",
    "ocl-icd-devel",
    "opencl-headers",
    "opusfile-devel",
    "pkgconf",
    "python",
    "python-zipfile-zstd",
    "python-zstandard",
    "sdl3-devel",
    "zstd-devel",
]
depends = [
    "cglm",
    "freetype",
    "gettext",
    "libpng",
    "libwebp",
    "mesa-opencl",
    "opusfile",
    "pkgconf",
    "python",
    "python-zipfile-zstd",
    "python-zstandard",
    "sdl3",
    "zlib-ng",
]

pkgdesc = "Open-source Touhou Project fangame"
license = "MIT"
url = "https://taisei-project.org"
source = [
    f"https://github.com/taisei-project/taisei/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/taisei-project/koishi/archive/{_koishi}.tar.gz",
    f"https://github.com/taisei-project/basis_universal/archive/{_basis_universal}.tar.gz",
    f"https://github.com/taisei-project/SDL_GameControllerDB/archive/{_gamecontrollerdb}.tar.gz",
]
source_paths = [
    ".",
    "external/koishi",
    "external/basis_universal",
    "external/gamecontrollerdb",
]
sha256 = [
    "748e9b45a0db0fd618165fe0dce56b518b908051932cb1c68731ae5ac32a8832",
    "1e5cb2f27325f7af6b06afa1f636a6585728afd36d3b5d8bebec98722b2df957",
    "7db7d535bee0842697dd98197f26c33f32e8f7cc0bab76c32697b2ad07f995dc",
    "9539ebf4f9b027565f981e1d725fa0ea7a7bb48a1bc386987829cf7c4f6d2b41",
]


def post_install(self):
    self.install_license("COPYING")
