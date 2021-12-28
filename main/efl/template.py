pkgname = "efl"
pkgver = "1.25.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbuild-tests=false",
    "-Dbuild-examples=false",
    "-Dembedded-lz4=false",
    "-Dcrypto=openssl",
    "-Decore-imf-loaders-disabler=ibus,scim",
    # FIXMEs:
    # enable pdf, ps, raw: libpoppler, libspectre, libraw
    # enable jp2k: libopenjpeg2
    # maybe enable avif
    "-Devas-loaders-disabler=avif,rsvg,json,pdf,ps,raw,jp2k",
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
hostmakedepends = ["meson", "pkgconf", "gettext-tiny-devel"]
makedepends = [
    "gettext-tiny-devel", "openssl-devel", "eudev-devel", "elogind-devel",
    "libmount-devel", "libdrm-devel", "libinput-devel", "libxkbcommon-devel",
    "mesa-devel", "wayland-protocols", "wayland-devel", "libxrandr-devel",
    "libxscrnsaver-devel", "libxcomposite-devel", "libxcursor-devel",
    "libxdamage-devel", "libxrender-devel", "libxext-devel", "libxtst-devel",
    "libxi-devel", "libxinerama-devel", "libxpresent-devel", "xcb-util-devel",
    "xcb-util-keysyms-devel", "xcb-util-image-devel", "xcb-util-wm-devel",
    "xcb-util-renderutil-devel", "xorgproto", "liblz4-devel", "zlib-devel",
    "fontconfig-devel", "fribidi-devel", "harfbuzz-devel", "freetype-devel",
    "libjpeg-turbo-devel", "libpng-devel", "giflib-devel", "libtiff-devel",
    "libwebp-devel", "libpulse-devel", "libsndfile-devel", "gstreamer-devel",
    "gst-plugins-base-devel", "glib-devel", "avahi-devel", "lua5.1-devel",
]
checkdepends = ["dbus", "xvfb-run", "check-devel"]
pkgdesc = "Enlightenment Foundation Libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND LGPL-2.1-only AND Zlib AND custom:small"
url = "https://enlightenment.org"
source = f"https://download.enlightenment.org/rel/libs/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "351ca0211ca000234527a503585f039f985607ec9439e34b49d8b8bbf35a7e6b"
# xvfb-run is unpackaged for now, and would need a special do_check
options = ["!check"]

match self.profile().arch:
    case "ppc64le" | "aarch64": # requires SSE3 on x86, so not there
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
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)
    self.rm(self.destdir / "usr/lib/ecore/system/systemd", recursive = True)

@subpackage("efl-devel")
def _devel(self):
    return self.default_devel()
