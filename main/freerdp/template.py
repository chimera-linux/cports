pkgname = "freerdp"
pkgver = "3.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_ALSA=OFF",
    "-DWITH_CAIRO=ON",
    "-DWITH_CHANNELS=ON",
    "-DWITH_JPEG=ON",
    "-DWITH_KRB5=ON",
    "-DWITH_MBEDTLS=OFF",
    "-DWITH_OSS=OFF",
    "-DWITH_PULSE=ON",
    "-DWITH_SERVER=ON",
    "-DWITH_SERVER_CHANNELS=ON",
    "-DWITH_SWSCALE=ON",
    "-DWITH_WAYLAND=ON",
    "-DWITH_WEBVIEW=OFF",
    "-DWITH_X11=ON",
    "-DWITH_ZLIB=ON",
    "-DWINPR_UTILS_IMAGE_JPEG=ON",
    "-DWINPR_UTILS_IMAGE_PNG=ON",
    "-DWINPR_UTILS_IMAGE_WEBP=ON",
]
hostmakedepends = [
    "cmake",
    "docbook-xsl",
    "ninja",
    "pkgconf",
    "wayland-progs",
    "xsltproc",
]
makedepends = [
    "cairo-devel",
    "cups-devel",
    "ffmpeg-devel",
    "fuse-devel",
    "gsm-devel",
    "heimdal-devel",
    "json-c-devel",
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libusb-devel",
    "libwebp-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "libxv-devel",
    "linux-headers",
    "openssl-devel",
    "pcsc-lite-devel",
    "pkcs11-helper-devel",
    "sdl-devel",
    "sdl_ttf-devel",
    "uriparser-devel",
    "wayland-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "RDP clients and libraries"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.freerdp.com"
source = f"https://pub.freerdp.com/releases/freerdp-{pkgver}.tar.gz"
sha256 = "2eef25f2b421dbe7b6ca64a96045afe57a4b8c559339baca8cb8528c42518b83"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}


@subpackage("freerdp-devel")
def _(self):
    return self.default_devel()


@subpackage("freerdp-libs")
def _(self):
    return self.default_libs()
