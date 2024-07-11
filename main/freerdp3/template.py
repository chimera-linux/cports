pkgname = "freerdp3"
pkgver = "3.6.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_ALSA=OFF",
    "-DWITH_CAIRO=ON",
    "-DWITH_CHANNELS=ON",
    "-DWITH_DSP_FFMPEG=ON",
    "-DWITH_FFMPEG=ON",
    "-DWITH_GSM=ON",
    "-DWITH_JPEG=ON",
    "-DWITH_LIBSYSTEMD=OFF",
    "-DWITH_MBEDTLS=OFF",
    "-DWITH_OSS=OFF",
    "-DWITH_SERVER=ON",
    "-DWITH_SERVER_CHANNELS=ON",
    "-DWITH_SOXR=ON",
    "-DWITH_SWSCALE=ON",
    "-DWITH_WEBVIEW=OFF",
    "-DWITH_ZLIB=ON",
    "-DBUILD_SHARED_LIBS=ON",
    # These are needed to avoid conflict with contrib/freerdp
    "-DWITH_BINARY_VERSIONING=ON",
    "-DRDTK_FORCE_STATIC_BUILD=ON",
    "-DUWAC_FORCE_STATIC_BUILD=ON",
]
hostmakedepends = ["cmake", "pkgconf", "ninja", "xsltproc", "docbook-xsl"]
makedepends = [
    "cairo-devel",
    "cups-devel",
    "ffmpeg-devel",
    "fuse-devel",
    "gsm-devel",
    "heimdal-devel",
    "icu-devel",
    "json-c-devel",
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
    "linux-pam-devel",
    "openssl-devel",
    "p11-kit-devel",
    "pcsc-lite-devel",
    "sdl-devel",
    "sdl_ttf-devel",
    "soxr-devel",
    "uriparser-devel",
    "wayland-devel",
]
pkgdesc = "RDP clients and libraries (version 3)"
maintainer = "triallax <triallax@tutanota.com>"
license = "Apache-2.0"
url = "https://www.freerdp.com"
source = f"https://github.com/FreeRDP/FreeRDP/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5c8b430ff20d0e367d4774248d52dc2d0feeb2b27af82feecfec0c702b41ab76"


@subpackage("freerdp3-devel")
def _devel(self):
    return self.default_devel()
