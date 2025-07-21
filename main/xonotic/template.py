pkgname = "xonotic"
pkgver = "0.8.6"
pkgrel = 1
build_style = "makefile"
make_use_env = True
makedepends = [
    "alsa-lib-devel",
    "curl-devel",
    "gmp-devel",
    "libjpeg-turbo-devel",
    "libmodplug-devel",
    "libvorbis-devel",
    "libxpm-devel",
    "libxxf86vm-devel",
    "mesa-devel",
    "sdl2-compat-devel",
]
depends = [f"xonotic-data~{pkgver}"]
pkgdesc = "Free, fast-paced cross-platform first-person shooter"
license = "GPL-2.0-or-later AND BSD-3-Clause"
url = "https://xonotic.org"
source = f"https://dl.xonotic.org/xonotic-{pkgver}-source.zip"
sha256 = "8b92ac781cff4ae89c121a23eacd7dec05a2aabedaccc23a19d1a0958b4012a8"
hardening = ["!int"]
# no tests
options = ["!check", "!cross"]

tool_flags = {
    "CFLAGS": ["-fno-math-errno", "-fno-rounding-math", "-fno-trapping-math"]
}


def configure(self):
    from cbuild.util import gnu_configure

    with self.pushd("source/d0_blind_id"):
        gnu_configure.replace_guess(self)
        gnu_configure.configure(self, configure_args=["--disable-rijndael"])


def build(self):
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


def install(self):
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
    for f in [22, 24, 32, 48, 64, 128, 256, 512]:
        self.install_file(
            f"misc/logos/icons_png/xonotic_{f}.png",
            f"usr/share/icons/hicolor/{f}x{f}/apps",
            name="xonotic.png",
        )
    self.install_file(
        "misc/logos/xonotic_icon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="xonotic.svg",
    )

    self.make.install(wrksrc="source/d0_blind_id")

    self.install_license("source/d0_blind_id/COPYING")

    self.uninstall("usr/include")
    self.uninstall("usr/lib/pkgconfig")
    self.uninstall("usr/lib/libd0_blind_id.a")
    self.uninstall("usr/lib/libd0_blind_id.so")
