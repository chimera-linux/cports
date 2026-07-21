pkgname = "taisei"
pkgver = "1.4.5"
# these are the submodules in the release tag
_koishi = "f899ac2f96051ffbc6cf9aa250f52832f0dfef9b"
_basis_universal = "380ef9389b38ec42506d5728dd05e94ac2f3c301"
_gamecontrollerdb = "7988b5e84c31616200ee2ffd2347386c6b3165a8"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dcpp_rtti=true",  # for basis_universal
    "-Ddefault_library=static",  # for libkoishi
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "shaderc-progs",
]
makedepends = [
    "boost-devel",  # fallback for koishi context backend on some archs
    "cglm-devel",
    "freetype-devel",
    "gamemode-devel",
    "libpng-devel",
    "libunibreak-devel",
    "libwebp-devel",
    "mesa-devel",
    "ocl-icd-devel",
    "openssl3-devel",
    "opus-devel",
    "opusfile-devel",
    "sdl3-devel",
    "zstd-devel",
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
    "776202314698fb83a2f38f0610dd6b6575a41f4478892f42e71fc80c9e3e5c04",
    "1e5cb2f27325f7af6b06afa1f636a6585728afd36d3b5d8bebec98722b2df957",
    "7db7d535bee0842697dd98197f26c33f32e8f7cc0bab76c32697b2ad07f995dc",
    "81bcf606f446c2d829fdd65830f8e8caaddade4b82e07029e91885d85832d870",
]


def post_install(self):
    self.install_license("COPYING.txt")
