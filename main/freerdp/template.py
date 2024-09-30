pkgname = "freerdp"
pkgver = "2.11.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_ALSA=OFF",
    "-DWITH_CAIRO=ON",
    "-DWITH_CHANNELS=ON",
    "-DWITH_JPEG=ON",
    "-DWITH_MBEDTLS=OFF",
    "-DWITH_OSS=OFF",
    "-DWITH_SERVER=ON",
    "-DWITH_SERVER_CHANNELS=ON",
    "-DWITH_SWSCALE=ON",
    "-DWITH_WEBVIEW=OFF",
    "-DWITH_ZLIB=ON",
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
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libusb-devel",
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
    "uriparser-devel",
    "wayland-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "RDP clients and libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://www.freerdp.com"
source = f"https://pub.freerdp.com/releases/freerdp-{pkgver}.tar.gz"
sha256 = "5a2d54e1ca0f1facd1632bcc94c73b9f071a80c5fdbbb3f26e79f02aaa586ca3"
patch_style = "patch"
tool_flags = {
    "CFLAGS": ["-DNDEBUG", "-Wno-incompatible-function-pointer-types"]
}


@subpackage("freerdp-devel")
def _(self):
    return self.default_devel()


@subpackage("freerdp-libs")
def _(self):
    return self.default_libs()
