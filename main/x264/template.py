pkgname = "x264"
_commit = "cde9a93319bea766a92e306d69059c76de970190"
pkgver = "20200702"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static", "--enable-shared"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "nasm", "perl", "bash"]
makedepends = ["fontconfig-devel", "fribidi-devel", "harfbuzz-devel"]
pkgdesc = "Free library for encoding H264/AVC video streams"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/x264.html"
source = (
    f"https://code.videolan.org/videolan/{pkgname}/-/archive/{_commit}.tar.gz"
)
sha256 = "8515baba9f82c723e07252747e9b0e166a16091ba72f2017387641724baec02d"
# guilty until proven wrong
hardening = ["!int"]
# no check target
options = ["!check"]

tool_flags = {"CFLAGS": ["-fPIC"]}

match self.profile().arch:
    case "x86_64":
        tools = {"AS": "nasm"}
    case _:
        tools = {"AS": "clang"}

match self.profile().endian:
    case "big":
        configure_env = {"CPU_ENDIAN": "big-endian"}
    case _:
        configure_env = {"CPU_ENDIAN": "little-endian"}


@subpackage("x264-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
