pkgname = "ffnvcodec-headers"
pkgver = "12.2.72.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "FFmpeg version of headers for Nvidia codec APIs"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/FFmpeg/nv-codec-headers"
source = f"{url}/releases/download/n{pkgver}/nv-codec-headers-{pkgver}.tar.gz"
sha256 = "c295a2ba8a06434d4bdc5c2208f8a825285210d71d91d572329b2c51fd0d4d03"
# No tests
options = ["!distlicense", "!check"]
