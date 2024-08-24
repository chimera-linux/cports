pkgname = "godot-export-templates-linux"
pkgver = "4.3"
pkgrel = 0
hostmakedepends = [
    "gettext",
    "pkgconf",
    "scons",
    "wayland-progs",
]
makedepends = [
    "libatomic-chimera-devel-static",
    "libcxx-devel-static",
    "libcxxabi-devel-static",
    "libunwind-devel-static",
    "linux-headers",
]
depends = []
pkgdesc = "2D and 3D game engine"
subdesc = "portable export templates for Linux"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://godotengine.org"
source = f"https://github.com/godotengine/godot/releases/download/{pkgver}-stable/godot-{pkgver}-stable.tar.xz"
sha256 = "751e55bfad8e04b846f9cf7b6eb80e058986a2cb1b103fc0fe6a4d8526a20e56"
# cross: why
options = ["!cross", "empty"]

# cbuild profile, godot arch
_targets = [
    ("x86_64", "x86_64"),
    ("armv7", "arm32"),
    ("aarch64", "arm64"),
    ("riscv64", "rv64"),
    # broken: ("ppc", "ppc32"),
    # executable name collides: ("ppc64", "ppc64"),
    ("ppc64le", "ppc64"),
]

_templates = [
    "debug",
    "release",
]

for _an, _ in _targets:
    if _an != self.profile().arch:
        hostmakedepends += [
            f"base-cross-{_an}",
            f"libatomic-chimera-cross-{_an}-static",
            f"libcxx-cross-{_an}-static",
            f"libcxxabi-cross-{_an}-static",
            f"libunwind-cross-{_an}-static",
            f"linux-headers-cross-{_an}",
        ]

_scons_flags = [
    "platform=linuxbsd",
    "production=yes",
    "use_llvm=yes",
    # use profile settings for lto
    "lto=none",
    # keep everything vendored so it's usable outside of chimera
]


def do_build(self):
    for an, godot_arch in _targets:
        for tmpl in _templates:
            self.log(f"building {tmpl} export template for {an}...")
            with self.profile(an) as pf:
                self.do(
                    "scons",
                    f"-j{self.make_jobs}",
                    "target=template_" + tmpl,
                    "arch=" + godot_arch,
                    *_scons_flags,
                    "CC=" + self.get_tool("CC"),
                    "CXX=" + self.get_tool("CXX"),
                    "LINK=" + self.get_tool("CXX"),
                    "cflags=" + self.get_cflags(shell=True),
                    "cxxflags=" + self.get_cxxflags(shell=True),
                    "linkflags=" + self.get_ldflags(shell=True),
                    env={
                        "BUILD_NAME": "chimera_linux",
                    },
                )


def do_install(self):
    self.install_license("LICENSE.txt")

    for _, godot_arch in _targets:
        for tmpl in _templates:
            # godot looks for export templates in $XDG_DATA_DIR/godot/export_templates/{pkgver}.stable
            # /usr/share could be the closest system-wide equivalent, but
            # cbuild does't like it. use /usr/lib instead.
            self.install_file(
                f"bin/godot.linuxbsd.template_{tmpl}.{godot_arch}.llvm",
                f"usr/lib/godot/export_templates/{pkgver}.stable",
                name=f"linux_{tmpl}.{godot_arch}",
            )


# use upstream naming convention
def _gen_subp(godot_arch):
    @subpackage(f"godot-export-templates-linux-{godot_arch}")
    def _(self):
        self.subdesc = f"portable export templates for {godot_arch} Linux"
        self.options = ["foreignelf"]

        return [f"usr/lib/godot/export_templates/*/linux_*.{godot_arch}"]


for _, _godot_arch in _targets:
    _gen_subp(_godot_arch)
    depends.append(
        self.with_pkgver(f"godot-export-templates-linux-{_godot_arch}")
    )
