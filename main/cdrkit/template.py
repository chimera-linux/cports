pkgname = "cdrkit"
pkgver = "1.1.11.5"
_debver = "-".join(pkgver.rsplit(".", 1))
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "libcap-progs", "ninja"]
makedepends = ["bzip2-devel", "libcap-devel", "zlib-ng-compat-devel"]
depends = ["!schilytools-cdrtools"]
pkgdesc = "Collection of CD/DVD authoring programs"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/debian/cdrkit"
source = (
    f"{url}/-/archive/debian/9%25{_debver}/cdrkit-debian-9%25{_debver}.tar.gz"
)
sha256 = "cd1781f29f8a98a3364727a242d9f243c695c563bc1cc072c548bb31349ca12f"
# old codebase, deharden...
tool_flags = {
    "CFLAGS": [
        "-fno-strict-aliasing",
        "-Wno-deprecated-non-prototype",
        "-D__THROW=",
    ]
}
file_modes = {
    "usr/bin/wodim": ("root", "root", 0o755),
    "usr/bin/icedax": ("root", "root", 0o755),
    "usr/bin/readom": ("root", "root", 0o755),
}

file_xattrs = {
    "usr/bin/wodim": {
        "security.capability": "cap_sys_resource,cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_ipc_lock,cap_sys_rawio+ep",
    },
    "usr/bin/icedax": {
        "security.capability": "cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_sys_rawio+ep",
    },
    "usr/bin/readom": {
        "security.capability": "cap_dac_override,cap_sys_admin,cap_net_bind_service,cap_sys_rawio+ep",
    },
}
hardening = ["!int"]
options = ["!lto"]


def post_install(self):
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="wodim.conf",
    )
    # compat symlinks
    self.install_link("usr/bin/mkisofs", "genisoimage")
    self.install_link("usr/share/man/man1/mkisofs.1", "genisoimage.1")
    self.install_link("usr/share/man/man1/cdda2mp3.1", "cdda2ogg.1")
    self.install_link("usr/bin/list_audio_tracks", "icedax")
    self.install_link("usr/bin/cdda2wav", "icedax")
    self.install_link("usr/share/man/man1/cdda2wav.1", "icedax.1")
    self.install_link("usr/bin/cdrecord", "wodim")
    self.install_link("usr/share/man/man1/cdrecord.1", "wodim.1")
    self.install_link("usr/share/man/man1/netscsid.1", "wodim.1")
