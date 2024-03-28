pkgname = "wireshark"
pkgver = "4.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_GNUTLS=ON",
    "-DENABLE_LUA=ON",
    "-DENABLE_DEBUG=OFF",
    "-DUSE_qt6=ON",
]
make_build_args = ["--target", "all", "test-programs"]
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "doxygen",
    "flex",
    "gettext-devel",
    "libcap-progs",
    "ninja",
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "c-ares-devel",
    "glib-devel",
    "gnutls-devel",
    "heimdal-devel",
    "libcap-devel",
    "libgcrypt-devel",
    "libnl-devel",
    "libpcap-devel",
    "libssh-devel",
    "libxml2-devel",
    "lua5.1-devel",
    "lz4-devel",
    "minizip-devel",
    "nghttp2-devel",
    "opus-devel",
    "pcre2-devel",
    "portaudio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "snappy-devel",
    "spandsp-devel",
    "speexdsp-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Network protocol analyzer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.wireshark.org"
source = f"https://www.wireshark.org/download/src/all-versions/wireshark-{pkgver}.tar.xz"
sha256 = "46bd0f4474337144b30816fb2d8f14e72a26d0391f24fe0b7b619acdcdad8c0c"
# forbid non-wireshark-group users from reading all network packets
file_modes = {
    "usr/bin/dumpcap": ("root", "_wireshark", 0o750),
}
file_xattrs = {
    "usr/bin/dumpcap": {
        "security.capability": "cap_net_raw,cap_net_admin+eip",
    },
}
# FIXME: cfi
hardening = ["vis"]

system_groups = ["_wireshark"]


def do_check(self):
    # extcaps can't work in our container
    self.do("pytest", "-k", "not TestExtcaps", wrksrc=self.make_dir)


def post_install(self):
    self.install_file(self.files_path / "wireshark.conf", "usr/lib/sysusers.d")
