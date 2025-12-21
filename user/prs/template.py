pkgname = "prs"
pkgver = "0.5.5"
pkgrel = 0
build_wrksrc = "cli"
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "dbus-devel",
    "gpgme-devel",
    "libgpg-error-devel",
    "openssl3-devel",
    "pcsc-lite-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Password manager CLI inspired by pass with multiple backends"
license = "GPL-3.0-only"
url = "https://timvisee.com/projects/prs"
source = (
    f"https://gitlab.com/timvisee/prs/-/archive/v{pkgver}/prs-v{pkgver}.tar.gz"
)
sha256 = "a38efc818ec75073bb7903c8992ce39d769478cb7435c9f43fcb9bbe75bd8189"
# Split into subpackages for backend selection, host binary for completion generation
options = ["empty", "!lintcomp", "!cross"]
_backends = [
    "gnupg-bin",
    "gpgme",
    "rpgpie",
]


def build(self):
    for backend in _backends:
        build_args = [
            "--no-default-features",
            "--features="
            + ",".join(
                [
                    f"backend-{backend}",
                    "alias",
                    "clipboard",
                    "notify",
                    "select-skim",
                    "select-fzf-bin",
                    "tomb",
                    "totp",
                ]
            ),
        ]

        self.cargo.build(args=build_args)
        self.mv(
            f"../target/{self.profile().triplet}/release/prs",
            f"prs-{backend}",
        )

    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"prs.{shell}", "w") as f:
            self.do("./prs-rpgpie", "internal", "completions", shell, stdout=f)


def install(self):
    for bin in [f"prs-{backend}" for backend in _backends]:
        self.install_bin(bin)

    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"prs.{shell}", shell)


def _create_backend_subpackage(_backend):
    @subpackage(f"prs-{_backend}")
    def _(self):
        self.depends = ["prs"] + [
            f"!prs-{backend}" for backend in _backends if backend != _backend
        ]
        if _backend == "gnupg-bin":
            self.install_if = [self.parent]

        def func():
            self.take(f"usr/bin/prs-{_backend}")
            self.mv(f">/usr/bin/prs-{_backend}", ">/usr/bin/prs")

        return func


for _backend in _backends:
    _create_backend_subpackage(_backend)
