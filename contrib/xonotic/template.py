pkgname = "xonotic"
pkgver = "0.8.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = [
    "gmp-devel",
    "mesa-devel",
    "sdl-devel",
    "libcurl-devel",
    "libmodplug-devel",
    "libvorbis-devel",
    "libxpm-devel",
    "libxxf86vm-devel",
    "libjpeg-turbo-devel",
    "alsa-lib-devel",
]
depends = ["desktop-file-utils", f"xonotic-data~{pkgver}"]
pkgdesc = "Free, fast-paced cross-platform first-person shooter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND BSD-3-Clause"
url = "https://xonotic.org"
source = f"https://dl.xonotic.org/{pkgname}-{pkgver}-source.zip"
sha256 = "a1a81ba55ab151bf09758e7f59614b2e5150e84224753e77950bcd07a282ea5d"
hardening = ["!int"]
# no tests
options = ["!check", "!cross"]

tool_flags = {
    "CFLAGS": ["-fno-math-errno", "-fno-rounding-math", "-fno-trapping-math"]
}


def do_configure(self):
    from cbuild.util import gnu_configure

    with self.pushd("source/d0_blind_id"):
        gnu_configure.replace_guess(self)
        gnu_configure.configure(self, configure_args=["--disable-rijndael"])


def do_build(self):
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)

    # build engine
    for p in ["cl", "sdl", "sv"]:
        self.make.invoke(
            [
                f"OPTIM_RELEASE={cfl} {ldfl}",
                f"{p}-release",
                "DP_LINK_TO_LIBJPEG=1",
                "DP_FS_BASEDIR=/usr/share/xonotic/",
                "CFLAGS_SSE=",
                "CFLAGS_SSE2=",
            ],
            wrksrc="source/darkplaces",
        )

    # d0_blind_id
    self.make.build(wrksrc="source/d0_blind_id")


def do_install(self):
    self.install_bin(
        "source/darkplaces/darkplaces-dedicated", name="xonotic-dedicated"
    )
    self.install_bin("source/darkplaces/darkplaces-glx", name="xonotic-glx")
    self.install_bin("source/darkplaces/darkplaces-sdl", name="xonotic-sdl")

    self.install_file(
        self.files_path / "xonotic-glx.desktop", "usr/share/applications"
    )
    self.install_file(
        self.files_path / "xonotic-sdl.desktop", "usr/share/applications"
    )
    self.install_file(
        "misc/logos/icons_png/xonotic_512.png",
        "usr/share/pixmaps",
        name="xonotic.png",
    )

    self.make.install(wrksrc="source/d0_blind_id")

    self.rm(self.destdir / "usr/include", recursive=True)
    self.rm(self.destdir / "usr/lib/pkgconfig", recursive=True)
    self.rm(self.destdir / "usr/lib/libd0_blind_id.a")
    self.rm(self.destdir / "usr/lib/libd0_blind_id.so")
