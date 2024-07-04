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
    "gettext-devel",
    "openssl-devel",
    "udev-devel",
    "elogind-devel",
    "libmount-devel",
    "libdrm-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "wayland-protocols",
    "wayland-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxrender-devel",
    "libxext-devel",
    "libxtst-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxpresent-devel",
    "xcb-util-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-image-devel",
    "xcb-util-wm-devel",
    "xcb-util-renderutil-devel",
    "xorgproto",
    "lz4-devel",
    "zlib-ng-compat-devel",
    "fontconfig-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "freetype-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "giflib-devel",
    "libjxl-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "libavif-devel",
    "libheif-devel",
    "libpulse-devel",
    "libraw-devel",
    "librsvg-devel",
    "libspectre-devel",
    "libpoppler-devel",
    "libsndfile-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "glib-devel",
    "avahi-devel",
    "lua5.1-devel",
    "ibus-devel",
]
checkdepends = [
    "dbus-x11",
    "xserver-xorg-xvfb",
    "mesa-dri",
    "fonts-dejavu-otf",
    "check-devel",
]
pkgdesc = "Enlightenment Foundation Libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND LGPL-2.1-only AND Zlib AND custom:small"
url = "https://enlightenment.org"
source = f"https://download.enlightenment.org/rel/libs/{pkgname}/{pkgname}-{pkgver}.tar.xz"
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
    self.pkgdesc = f"{pkgdesc} (IBus support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ibus"]

    return ["usr/lib/ecore_imf/modules/ibus"]


@subpackage("efl-devel")
def _devel(self):
    return self.default_devel()
