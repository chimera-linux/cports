pkgname = "graphicsmagick"
pkgver = "1.3.45"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-shared",
    "--with-bzlib",
    "--with-gs-font-dir=/usr/share/fonts/Type1",
    "--with-jbig",
    "--with-jp2",
    "--with-jxl",
    "--with-heif",
    "--with-lcms2",
    "--with-lzma",
    "--with-modules",
    "--with-perl",
    "--with-png",
    "--with-quantum-depth=16",
    "--with-threads",
    "--with-tiff",
    "--with-ttf",
    "--with-webp",
    "--with-x",
    "--with-zlib",
    "--with-zstd",
]
hostmakedepends = [
    "automake",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "jasper-devel",
    "jbigkit-devel",
    "lcms2-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "libtiff-devel",
    "libtool-devel",
    "libwebp-devel",
    "libxml2-devel",
    "xz-devel",
    "zstd-devel",
]
pkgdesc = "Image processing system"
license = "MIT"
url = "http://www.graphicsmagick.org"
source = f"$(SOURCEFORGE_SITE)/graphicsmagick/GraphicsMagick-{pkgver}.tar.xz"
sha256 = "dcea5167414f7c805557de2d7a47a9b3147bcbf617b91f5f0f4afe5e6543026b"

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]


def post_install(self):
    self.install_license("Copyright.txt")


@subpackage("graphicsmagick-devel")
def _(self):
    return self.default_devel()
