pkgname = "polkit"
pkgver = "121"
pkgrel = 4
build_style = "meson"
configure_args = [
    "-Dsession_tracking=libelogind",
    "-Dsystemdsystemunitdir=/tmp",
    "-Dpolkitd_user=_polkitd",
    "-Djs_engine=duktape",
    "-Dauthfw=pam",
    "-Dpam_include=dummy",
    "-Dos_type=redhat",  # dummy value
    "-Dman=true",
    "-Dintrospection=true",
    "-Dtests=false",  # tests need mocklibc
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "gettext-tiny",
    "glib-devel",
    "perl",
    "xsltproc",
    "docbook-xsl-nons",
]
makedepends = ["elogind-devel", "duktape-devel", "linux-pam-devel"]
pkgdesc = "Toolkit for defining and handling authorizations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/polkit"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "9dc7ae341a797c994a5a36da21963f0c5c8e3e5a1780ccc2a5f52e7be01affaa"
suid_files = [
    "usr/lib/polkit-1/polkit-agent-helper-1",
    "usr/bin/pkexec",
]
# tests are broken on musl
options = ["!check"]

system_users = ["_polkitd"]


def post_install(self):
    self.rm(self.destdir / "tmp", recursive=True)
    self.rm(self.destdir / "etc/pam.d/polkit-1")
    self.install_file(
        self.files_path / "polkit-1.pam", "etc/pam.d", name="polkit-1"
    )
    self.install_service(self.files_path / "polkitd")
    # move defaults
    rsrc = self.destdir / "etc/polkit-1/rules.d"
    rdest = self.destdir / "usr/share/polkit-1/rules.d"
    self.mv(rsrc / "50-default.rules", rdest)
    rdest.chmod(0o755)


@subpackage("polkit-devel")
def _devel(self):
    return self.default_devel()
