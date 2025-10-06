pkgname = "godot"
pkgver = "4.4.1"
pkgrel = 6
hostmakedepends = [
    "gettext",
    "pkgconf",
    "scons",
    "wayland-progs",
]
makedepends = [
    "brotli-devel",
    "dbus-devel",
    "enet-devel",
    "freetype-devel",
    "glslang-devel",
    "graphite2-devel",
    "libdecor-devel",
    "libogg-devel",
    "libpng-devel",
    "libpulse-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "mbedtls-devel",
    "miniupnpc-devel",
    "pcre2-devel",
    "speechd-devel",
    "udev-devel",
    "wayland-devel",
    "wslay-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "2D and 3D game engine"
subdesc = "GUI editor"
license = "MIT"
url = "https://godotengine.org"
source = f"https://github.com/godotengine/godot/releases/download/{pkgver}-stable/godot-{pkgver}-stable.tar.xz"
sha256 = "ddbd6527cdb3ddb02910b383301a5c9117b1c33c777ef1c86d1b1eea43dcb651"
# cross: nah
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "SafeNumeric seemingly unimplemented"

match self.profile().arch:
    case "x86_64":
        _godot_arch = "x86_64"
    case "armv7":
        _godot_arch = "arm32"
    case "aarch64":
        _godot_arch = "arm64"
    case "riscv64":
        _godot_arch = "rv64"
    case "ppc":
        _godot_arch = "ppc32"
    case "ppc64" | "ppc64le":
        _godot_arch = "ppc64"
    case _:
        _godot_arch = ""
        broken = f"{self.profile().arch} is unsupported"

_scons_flags = [
    "platform=linuxbsd",
    "arch=" + _godot_arch,
    "production=yes",
    "use_llvm=yes",
    "use_static_cpp=no",
    # use profile settings for lto
    "lto=none",
    "engine_update_check=false",
    # don't dlopen system libraries
    "use_sowrap=false",
    "alsa=false",
    "x11=false",
    # devendored:
    "builtin_brotli=false",
    "builtin_certs=false",
    "builtin_enet=false",
    "builtin_freetype=false",
    "builtin_glslang=false",
    "builtin_graphite=false",
    "builtin_libogg=false",
    "builtin_libpng=false",
    "builtin_libtheora=false",
    "builtin_libvorbis=false",
    "builtin_libwebp=false",
    "builtin_mbedtls=false",
    "builtin_miniupnpc=false",
    "builtin_pcre2=false",
    "builtin_wslay=false",
    "builtin_zlib=false",
    "builtin_zstd=false",
    # https://github.com/godotengine/godot/issues/91401
    "builtin_harfbuzz=true",
    # https://github.com/godotengine/godot/issues/91401
    # https://github.com/godotengine/godot/issues/100301
    "builtin_icu4c=true",
    # also kept vendored:
    "builtin_clipper2=true",
    "builtin_msdfgen=true",
    "builtin_openxr=true",
    "builtin_recastnavigation=true",
    "builtin_rvo2_2d=true",
    "builtin_rvo2_3d=true",
    "builtin_squish=true",
    "builtin_xatlas=true",
]


if self.profile().arch in ["aarch64", "x86_64"]:
    makedepends += ["embree-devel"]
    _scons_flags += ["builtin_embree=false"]


def build(self):
    for target in ["editor", "template_debug", "template_release"]:
        self.do(
            "scons",
            f"-j{self.make_jobs}",
            "target=" + target,
            *_scons_flags,
            "cflags=" + self.get_cflags(shell=True),
            "cxxflags=" + self.get_cxxflags(shell=True),
            "linkflags=" + self.get_ldflags(shell=True),
            "import_env_vars=CCACHE_DIR",  # fuck you scons
            env={
                "BUILD_NAME": "chimera_linux",
            },
        )


def install(self):
    self.install_license("LICENSE.txt")
    self.install_file(
        "misc/dist/linux/org.godotengine.Godot.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "misc/dist/linux/org.godotengine.Godot.appdata.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "misc/dist/linux/org.godotengine.Godot.xml", "usr/share/mime/packages"
    )
    self.install_file(
        "icon.png", "usr/share/icons/hicolor/256x256/apps", name="godot.png"
    )
    self.install_file(
        "icon.svg", "usr/share/icons/hicolor/scalable/apps", name="godot.svg"
    )
    self.install_man("misc/dist/linux/godot.6")
    self.install_bin(
        f"bin/godot.linuxbsd.editor.{_godot_arch}.llvm", name="godot"
    )
    # same naming as alpine
    self.install_bin(
        f"bin/godot.linuxbsd.template_debug.{_godot_arch}.llvm",
        name="godot-template-debug",
    )
    self.install_bin(
        f"bin/godot.linuxbsd.template_release.{_godot_arch}.llvm",
        name="godot-template-release",
    )


@subpackage("godot-export-templates")
def _(self):
    self.subdesc = "export templates"

    return ["usr/bin/godot-template-*"]
