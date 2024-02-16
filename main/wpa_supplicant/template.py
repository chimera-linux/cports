pkgname = "wpa_supplicant"
pkgver = "2.10"
pkgrel = 3
build_wrksrc = pkgname
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["V=1"]
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "libnl-devel",
    "openssl-devel",
    "dbus-devel",
    "libedit-readline-devel",
    "linux-headers",
]
pkgdesc = "WPA/WPA2/IEEE 802.1X Supplicant"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://w1.fi/wpa_supplicant"
source = f"http://w1.fi/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "20df7ae5154b3830355f8ab4269123a87affdea59fe74fe9292a91d0d7e17b2f"
# no test suite?
options = ["!check"]


def post_patch(self):
    self.cp(self.files_path / "config", "wpa_supplicant/.config")


def pre_install(self):
    self.install_dir("usr/bin")


def post_install(self):
    # dbus services
    for f in (self.cwd / "dbus").glob("*.service"):
        self.install_file(f, "usr/share/dbus-1/system-services")
    # dbus config
    self.install_file(
        "dbus/dbus-wpa_supplicant.conf",
        "usr/share/dbus-1/system.d",
        name="wpa_supplicant.conf",
    )
    # default config
    self.install_file(
        self.files_path / "wpa_supplicant.conf",
        "etc/wpa_supplicant",
        mode=0o640,
    )
    # manpages
    for m in (self.cwd / "doc/docbook").glob("*.[58]"):
        if (
            m.stem == "wpa_gui"
            or m.stem == "wpa_priv"
            or m.stem == "eapol_test"
        ):
            continue
        self.install_man(m)
    # license
    self.install_license("README")
