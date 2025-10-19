pkgname = "wireshark"
pkgver = "4.4.8"
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
    "lua5.4-devel",
    "lz4-devel",
    "minizip-ng-devel",
    "nghttp2-devel",
    "nghttp3-devel",
    "opus-devel",
    "pcre2-devel",
    "portaudio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "sbc-devel",
    "snappy-devel",
    "spandsp-devel",
    "speexdsp-devel",
    "zlib-ng-devel",
    "zstd-devel",
]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Network protocol analyzer"
license = "GPL-2.0-or-later"
url = "https://www.wireshark.org"
source = f"https://www.wireshark.org/download/src/all-versions/wireshark-{pkgver}.tar.xz"
sha256 = "dd648c5c5994843205cd73e57d6673f6f4e12718e1c558c674cb8bdafeacde47"
file_modes = {
    "usr/bin/dumpcap": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/dumpcap": {
        "security.capability": "cap_net_raw,cap_net_admin+ep",
    },
}
hardening = ["vis", "!cfi"]


def check(self):
    # extcaps can't work in our container
    self.do(
        "pytest",
        "-k",
        "not TestExtcaps",
        "--dist=worksteal",
        wrksrc=self.make_dir,
    )


def post_install(self):
    self.install_sysusers("^/wireshark.conf")
