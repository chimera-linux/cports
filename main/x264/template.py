pkgname = "x264"
_commit = "0480cb05fa188d37ae87e8f4fd8f1aea3711f7ee"
pkgver = "20250831"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static", "--enable-shared"]
configure_gen = []
hostmakedepends = ["bash", "nasm", "perl", "pkgconf"]
makedepends = ["fontconfig-devel", "fribidi-devel", "harfbuzz-devel"]
pkgdesc = "Free library for encoding H264/AVC video streams"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/x264.html"
source = f"https://code.videolan.org/videolan/x264/-/archive/{_commit}.tar.gz"
sha256 = "d0967a1348c85dfde363bb52610403be898171493100561efa0dd05d5fd1ae50"
# no check target
# lto: miscompiles on some targets
options = ["!check", "!lto"]

match self.profile.arch:
    case "x86_64":
        tools = {"AS": "nasm"}
    case _:
        tools = {"AS": "clang"}

match self.profile.endian:
    case "big":
        configure_env = {"CPU_ENDIAN": "big-endian"}
    case _:
        configure_env = {"CPU_ENDIAN": "little-endian"}


@subpackage("x264-devel")
def _(self):
    return self.default_devel()
