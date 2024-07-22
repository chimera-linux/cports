pkgname = "efl"
pkgver = "1.27.0"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dbuild-tests=false",  # enable if enabling tests
    "-Dbuild-examples=false",
    "-Dembedded-lz4=false",
    "-Dcrypto=openssl",
    "-Decore-imf-loaders-disabler=scim",
    # rlottie (json) is pretty useless and unstable so keep that off
    "-Devas-loaders-disabler=json",
    "-Dlua-interpreter=lua",
    "-Dbindings=cxx",
    "-Dopengl=es-egl",
    "-Dphysics=false",
    "-Delua=false",
    "-Dsystemd=true",
    "-Dx11=true",
    "-Dxpresent=true",
    "-Dxinput2=true",
    "-Dxinput22=true",
    "-Dfb=true",
    "-Dwl=true",
    "-Ddrm=true",
    "-Dgstreamer=true",
    "-Dpulseaudio=true",
    "-Dharfbuzz=true",
    "-Dglib=true",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["meson", "pkgconf", "gettext-devel"]
makedepends = [
    "avahi-devel",
    "elogind-devel",
    "fontconfig-devel",
    "freetype-devel",
    "fribidi-devel",
    "gettext-devel",
    "giflib-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "harfbuzz-devel",
    "ibus-devel",
    "libavif-devel",
    "libdrm-devel",
    "libheif-devel",
    "libinput-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libmount-devel",
    "libpng-devel",
    "libpoppler-devel",
    "libpulse-devel",
    "libraw-devel",
    "librsvg-devel",
    "libsndfile-devel",
    "libspectre-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxpresent-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxscrnsaver-devel",
    "libxtst-devel",
    "lua5.1-devel",
    "lz4-devel",
    "mesa-devel",
    "openjpeg-devel",
    "openssl-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
    "xorgproto",
    "zlib-ng-compat-devel",
]
checkdepends = [
    "check-devel",
    "dbus-x11",
    "fonts-dejavu-otf",
    "mesa-dri",
    "xserver-xorg-xvfb",
]
pkgdesc = "Enlightenment Foundation Libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND LGPL-2.1-only AND Zlib AND custom:small"
url = "https://enlightenment.org"
source = f"https://download.enlightenment.org/rel/libs/efl/efl-{pkgver}.tar.xz"
sha256 = "3dfb99fbcc268c0bc797e2f83e8c503ef9de66284f40b381bb597a08185c00f4"
tool_flags = {"CFLAGS": ["-D_LARGEFILE64_SOURCE", "-D__USE_MISC"]}
# FIXME int: janky codebase
hardening = ["!int"]
# some suites are in a bad shape
options = ["!check"]

match self.profile().arch:
    case "ppc64le" | "aarch64":  # requires SSE3 on x86, so not there
        configure_args.append("-Dnative-arch-optimization=true")
    case _:
        configure_args.append("-Dnative-arch-optimization=false")

if self.profile().cross:
    hostmakedepends.append("efl-devel")


def post_install(self):
    self.install_license("licenses/COPYING.BSD")
    self.install_license("licenses/COPYING.SMALL")
    self.install_license("licenses/COPYING.DNS")

    # service files: maybe reimplement for dinit later
    self.uninstall("usr/lib/systemd")
    self.uninstall("usr/lib/ecore/system/systemd")


@subpackage("efl-ibus")
def _ibus(self):
    self.subdesc = "IBus support"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ibus"]

    return ["usr/lib/ecore_imf/modules/ibus"]


@subpackage("efl-devel")
def _devel(self):
    return self.default_devel()
