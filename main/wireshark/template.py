pkgname = "wireshark"
pkgver = "4.4.2"
pkgrel = 1
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
scripts = {"pre-install": True}
pkgdesc = "Network protocol analyzer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.wireshark.org"
source = f"https://www.wireshark.org/download/src/wireshark-{pkgver}.tar.xz"
sha256 = "6053d97499c83feb87ce1d7f732d9c889c6c18bb334de67e65dca11483b0514e"
# forbid non-wireshark-group users from reading all network packets
file_modes = {
    "usr/bin/dumpcap": ("root", "_wireshark", 0o750),
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
    self.install_sysusers(self.files_path / "wireshark.conf")
