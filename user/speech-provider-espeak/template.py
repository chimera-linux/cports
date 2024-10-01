pkgname = "speech-provider-espeak"
pkgver = "0_git20240718"
pkgrel = 0
_gitrev = "147125c649498c0eec3d3872364257b2be53ea0b"
build_style = "meson"
hostmakedepends = ["cargo-auditable", "meson", "pkgconf"]
makedepends = [
    "espeak-ng-devel",
    "glib-devel",
    "libspeechprovider-devel",
    "libspiel-devel",
    "rust-std",
]
pkgdesc = "Spiel speech provider using eSpeak-NG"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://project-spiel.org"
source = f"https://github.com/project-spiel/speech-provider-espeak/archive/{_gitrev}.tar.gz"
sha256 = "f66275d7bbd4f8689105680f43537cbadcb3c49446bf9adbad1a9c9cbd96330e"
# no tests
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/speech-provider-espeak",
    )
