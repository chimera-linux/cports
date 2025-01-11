pkgname = "transmission"
pkgver = "4.0.6"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DENABLE_DAEMON=ON",
    "-DENABLE_GTK=ON",
    "-DENABLE_QT=ON",
    "-DENABLE_CLI=ON",
    "-DINSTALL_LIB=ON",
    "-DUSE_SYSTEM_DEFLATE=ON",
    "-DUSE_SYSTEM_EVENT2=ON",
    "-DUSE_SYSTEM_MINIUPNPC=ON",
    "-DUSE_SYSTEM_PSL=ON",
    "-DUSE_SYSTEM_GTEST=ON",
]
# needs net
make_check_args = ["-E", "LT.DhtTest.usesBootstrapFile"]
hostmakedepends = [
    "cmake",
    "gettext",
    "libxml2-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtest-devel",
    "gtkmm-devel",
    "curl-devel",
    "libdeflate-devel",
    "libevent-devel",
    "libpsl-devel",
    "linux-headers",
    "miniupnpc-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "BitTorrent client"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/transmission/transmission"
source = f"{url}/releases/download/{pkgver}/transmission-{pkgver}.tar.xz"
sha256 = "2a38fe6d8a23991680b691c277a335f8875bdeca2b97c6b26b598bc9c7b0c45f"


def pre_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "transmission-daemon")


@subpackage("transmission-devel-static")
def _(self):
    return ["lib:libtransmission.a"]


@subpackage("transmission-devel")
def _(self):
    # static-only lib so just pull it
    self.depends = [self.with_pkgver("transmission-devel-static")]
    return self.default_devel()


@subpackage("transmission-daemon")
def _(self):
    self.subdesc = "daemon"
    return [
        "cmd:transmission-daemon",
        "usr/lib/dinit.d/transmission-daemon",
        "usr/lib/sysusers.d/transmission.conf",
        "usr/lib/tmpfiles.d/transmission.conf",
        "usr/share/transmission/public_html",
    ]


@subpackage("transmission-qt")
def _(self):
    self.subdesc = "QT client"
    # icons left in base package
    self.depends = [self.parent]
    return [
        "cmd:transmission-qt",
        "usr/share/applications/transmission-qt.desktop",
        "usr/share/transmission/translations",
    ]


@subpackage("transmission-gtk")
def _(self):
    self.subdesc = "GTK client"
    # icons left in base package
    self.depends = [self.parent]
    return [
        "cmd:transmission-gtk",
        "usr/share/applications/transmission-gtk.desktop",
        "usr/share/locale",
        "usr/share/metainfo/transmission-gtk.metainfo.xml",
    ]


@subpackage("transmission-progs")
def _(self):
    self.subdesc = "CLI tools"
    return [
        "cmd:transmission-cli",
        "cmd:transmission-edit",
        "cmd:transmission-show",
        "cmd:transmission-create",
        "cmd:transmission-remote",
    ]
