pkgname = "gleam"
pkgver = "1.16.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # overflows the stack on ppc64le
    "--skip=type_::tests::no_stack_overflow_for_nested_use",
]
hostmakedepends = ["cargo-auditable"]
checkdepends = ["erlang", "git", "nodejs"]
depends = ["erlang"]
pkgdesc = "Friendly language for building scalable type-safe systems"
license = "Apache-2.0"
url = "https://gleam.run"
source = (
    f"https://github.com/gleam-lang/gleam/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "dd676c5faff4963d7a26683b164788a09f1261326bcb1c7fc20e001ed3843c30"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
