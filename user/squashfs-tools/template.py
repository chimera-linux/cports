pkgname = "squashfs-tools"
pkgver = "4.6.1"
pkgrel = 0
build_wrksrc = "squashfs-tools"
build_style = "makefile"
make_build_args = [
    "XZ_SUPPORT=1",
    "LZO_SUPPORT=1",
    "LZMA_XZ_SUPPORT=1",
    "LZ4_SUPPORT=1",
    "ZSTD_SUPPORT=1",
]
make_install_args = [
    "INSTALL_PREFIX=$(DESTDIR)/usr",
    "INSTALL_MANPAGES_DIR=$(DESTDIR)/usr/share/man/man1",
]
make_use_env = True
makedepends = [
    "bzip2-devel",
    "lz4-devel",
    "lzo-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Tools to create and extract Squashfs filesystems"
maintainer = "tj <tjheeta@gmail.com>"
license = "GPL-2.0-only"
url = "https://github.com/plougher/squashfs-tools"
source = f"https://github.com/plougher/squashfs-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "94201754b36121a9f022a190c75f718441df15402df32c2b520ca331a107511c"
# no tests
options = ["!check"]
