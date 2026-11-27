pkgname = "subrandr"
pkgver = "1.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "rust-std",
]
pkgdesc = "Rendering library for non-ASS subtitles"
license = "MPL-2.0"
url = "https://github.com/afishhh/subrandr"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5390036167744287d27e808029121e5d2fed57847685dfef5c3e413bddf17a72"


def build(self):
    from cbuild.util import cargo

    cargo.Cargo(self).invoke("run", ["-p", "xtask", "--", "build"])


def install(self):
    from cbuild.util import cargo

    cargo.Cargo(self).invoke(
        "run",
        [
            "-p",
            "xtask",
            "--",
            "install",
            "--prefix",
            "/usr",
            "--destdir",
            f"{self.chroot_destdir}/usr",
        ],
    )


@subpackage("subrandr-devel")
def _(self):
    return self.default_devel()
