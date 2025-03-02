pkgname = "speech-provider-espeak"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["cargo-auditable", "meson", "pkgconf"]
makedepends = [
    "espeak-ng-devel",
    "glib-devel",
    "libspeechprovider-devel",
    "rust-std",
]
pkgdesc = "Spiel speech provider using eSpeak-NG"
license = "GPL-3.0-or-later"
url = "https://project-spiel.org"
source = f"https://github.com/project-spiel/speech-provider-espeak/archive/refs/tags/SPEECH_PROVIDER_ESPEAK_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "1ef78b61a8792f5fd2f1b85ad8384d9e810e081c02668c40701aa00115e9503e"
# no tests
options = ["!check"]


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


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
