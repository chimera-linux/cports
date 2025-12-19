pkgname = "efl"
pkgver = "1.28.1"
pkgrel = 0
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
make_check_wrapper = ["xwayland-run"]
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
    "libpng-devel",
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
    "openssl3-devel",
    "poppler-devel",
    "udev-devel",
    "util-linux-mount-devel",
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
    "xwayland-run",
]
pkgdesc = "Enlightenment Foundation Libraries"
license = "BSD-2-Clause AND LGPL-2.1-only AND Zlib AND custom:small"
url = "https://enlightenment.org"
source = f"https://download.enlightenment.org/rel/libs/efl/efl-{pkgver}.tar.xz"
sha256 = "84cf6145f9cc82bfff690005be24392c8f3c52f8e00ff04d8eea371429c09424"
tool_flags = {
    "CFLAGS": ["-D_LARGEFILE64_SOURCE", "-D__USE_MISC"],
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
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
def _(self):
    self.subdesc = "IBus support"
    self.install_if = [self.parent, "ibus"]

    return ["usr/lib/ecore_imf/modules/ibus"]


@subpackage("efl-devel")
def _(self):
    return self.default_devel()
