pkgname = "gmid"
pkgver = "2.1.1"
pkgrel = 0
build_style = "configure"
configure_args = ["PREFIX=/usr", "MANDIR=/usr/share/man"]
make_check_target = "regress"
hostmakedepends = ["flex", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "libretls-devel",
    "openssl3-devel",
]
checkdepends = [
    "ca-certificates",
    "openssh",
    "procps",
]
pkgdesc = "Gemini server"
license = "ISC"
url = "https://gmid.omarpolo.com"
source = f"https://ftp.omarpolo.com/gmid-{pkgver}.tar.gz"
sha256 = "9eb0fe4272616e71ef28adb1a10808adb58db01626acc39fddebf58e0a0ac4bf"
tool_flags = {"CFLAGS": ["-Wno-deprecated-declarations"]}


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "gmid")


@subpackage("gmid-progs")
def _(self):
    return ["cmd:gemexp", "cmd:gg", "cmd:titan"]
