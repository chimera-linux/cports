pkgname = "spice-vdagent"
pkgver = "0.22.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-session-info=none"]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    "glib-devel",
    "libdrm-devel",
    "libxfixes-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "spice-protocol",
]
checkdepends = ["procps"]
depends = ["dbus"]
pkgdesc = "SPICE VDAgent for Linux guests"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://www.spice-space.org"
source = f"https://www.spice-space.org/download/releases/spice-vdagent-{pkgver}.tar.bz2"
sha256 = "93b0d15aca4762cc7d379b179a7101149dbaed62b72112fffb2b3e90b11687a0"
hardening = ["vis", "cfi"]


def post_install(self):
    # tmpfiles.d
    self.install_file(
        "data/tmpfiles.d/spice-vdagentd.conf", "usr/lib/tmpfiles.d"
    )
    # dinit
    self.install_service(self.files_path / "spice-vdagentd")
    # drop GDM integration files which break XDG autostarted spice-vdagent for the logged in user
    self.rm(self.destdir / "usr/share/gdm", recursive=True)
