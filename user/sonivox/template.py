pkgname = "sonivox"
pkgver = "3.6.16"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SONIVOX_STATIC=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "MIDI synthesizer library"
license = "Apache-2.0"
url = "https://github.com/pedrolcl/sonivox"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!https://www.ronimusic.com/sf2/Airfont_340.dls>sonivox-{pkgver}-soundfont.dls",
]
sha256 = [
    "8e9adf39a5e60c5b9ce4d1b79c83680cfab97d6e8eec6ffb6a3d0bad41413531",
    "beb3e39e3c9fc51ef4dff36fdd8db0361471a91d244c3ee78af90f6d3c783b04",
]


def post_extract(self):
    self.mkdir("build/tmp", parents=True)
    self.mv(
        self.sources_path / f"sonivox-{pkgver}-soundfont.dls",
        "build/tmp/soundfont.dls",
    )


def init_configure(self):
    self.configure_env = {"TEMP": str(self.chroot_cwd / "build/tmp")}


def init_check(self):
    self.make_check_env.update(self.configure_env)


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
