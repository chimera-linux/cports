# AGPL: forbidden from being a dependency except in special unambiguous cases
pkgname = "ghostscript"
pkgver = "10.03.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-dynamic",
    "--enable-fontconfig",
    "--enable-freetype",
    "--enable-openjpeg",
    "--enable-cups",
    "--disable-compile-inits",
    "--with-ijs",
    "--with-system-libtiff",
    "--with-libpaper",
    "--with-x",
    "--with-jbig2dec",
    "--with-drivers=ALL",
    "--with-fontpath=/usr/share/fonts/Type1:/usr/share/fonts",
]
configure_env = {
    "CUPSCONFIG": "/usr/bin/cups-config",
    "CCAUX": "cc",
}
configure_gen = []
make_cmd = "gmake"
make_dir = "."  # bad build system
make_build_args = ["all", "so"]
make_install_args = ["install", "install-so"]
hostmakedepends = ["pkgconf", "gmake"]
makedepends = [
    "cups-devel",
    "dbus-devel",
    "fontconfig-devel",
    "jasper-devel",
    "jbig2dec-devel",
    "openjpeg-devel",
    "lcms2-devel",
    "libxext-devel",
    "libxt-devel",
    "libpaper-devel",
    "ijs-devel",
    "zlib-devel",
]
pkgdesc = "PostScript and PDF language interpreter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "AGPL-3.0-or-later"
url = "https://www.ghostscript.com"
source = f"https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs{pkgver.replace('.', '')}/ghostscript-{pkgver}.tar.xz"
sha256 = "f25ff491a726d883f0b0f9c8af9b895c674cf77cddd814aa3824b3223f439ee5"
# breaks ps2pdf
hardening = ["!int"]
# busted; undefined references
options = ["!lto"]

if self.profile().cross:
    hostmakedepends += makedepends


def post_patch(self):
    for f in [
        "cups/libs",
        "freetype",
        "ijs",
        "jbig2dec",
        "jpeg",
        "lcms2mt",
        "libpng",
        "openjpeg",
        "tiff",
        "zlib",
    ]:
        self.rm(f, recursive=True)


def init_configure(self):
    self.configure_env["CFLAGSAUX"] = self.get_cflags(target="host", shell=True)
    # work around terrible build system
    self.configure_env["LDFLAGS"] = (
        self.get_cflags(shell=True) + " " + self.get_ldflags(shell=True)
    )


def init_install(self):
    self.make_install_args += [
        "cups_serverroot=" + str(self.chroot_destdir / "etc/cups"),
        "cups_serverbin=" + str(self.chroot_destdir / "usr/lib/cups"),
    ]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libgs")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("libgs-devel")
def _devel(self):
    return self.default_devel()
