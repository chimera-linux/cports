pkgname = "libglvnd"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtls=false"]
make_check_wrapper = ["wlheadless-run", "--", "xwayland-run", "--"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "libx11-devel",
    "libxext-devel",
    "xorgproto",
]
checkdepends = ["xwayland-run"]
# transitional providers, with high enough versions to be safe
renames = [
    "libegl=26.3",
    "libgl=26.3",
    "libgles1=26.3",
    "libgles2=26.3",
    "mesa-egl-libs=26.3",
    "mesa-gl-libs=26.3",
    "mesa-gles1-libs=26.3",
    "mesa-gles2-libs=26.3",
]
pkgdesc = "GL vendor-neutral dispatch library"
license = "custom:glvnd"
url = "https://gitlab.freedesktop.org/glvnd/libglvnd"
source = f"{url}/-/archive/v{pkgver}/libglvnd-v{pkgver}.tar.gz"
sha256 = "2b6e15b06aafb4c0b6e2348124808cbd9b291c647299eaaba2e3202f51ff2f3d"
# cyclic checkdepends (xwayland-run needs compositor which needs gl headers...)
options = ["!check"]


def post_install(self):
    self.install_license("README.md")


@subpackage("libglvnd-devel")
def _(self):
    # pre-transition mesa has conflicting files
    self.depends += ["!mesa-devel<26.2.5-r1"]

    return self.default_devel()
