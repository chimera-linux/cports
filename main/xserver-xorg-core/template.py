pkgname = "xserver-xorg-core"
pkgver = "21.1.14"
pkgrel = 1
build_style = "meson"
_fontroot = "/usr/share/fonts"
configure_args = [
    "-Dxorg=true",
    "-Dxephyr=true",
    "-Dxnest=true",
    "-Dxvfb=true",
    "-Dipv6=true",
    "-Dxcsecurity=true",
    "-Ddri3=true",
    "-Dglamor=true",
    "-Dglx=true",
    "-Dseatd_libseat=true",
    "-Dsuid_wrapper=true",
    "-Dlinux_acpi=true",
    "-Dudev=true",
    "-Dlinux_apm=false",
    "-Dhal=false",
    "-Dsystemd_logind=false",
    "-Dxkb_dir=/usr/share/X11/xkb",
    "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "xkbcomp", "flex"]
makedepends = [
    "libxfont2-devel",
    "libxkbfile-devel",
    "libxshmfence-devel",
    "libxcb-devel",
    "libxrender-devel",
    "libxv-devel",
    "libxtst-devel",
    "libxres-devel",
    "libxxf86dga-devel",
    "libxkbui-devel",
    "libtirpc-devel",
    "libseat-devel",
    "mesa-devel",
    "libepoxy-devel",
    "pixman-devel",
    "nettle-devel",
    "dbus-devel",
    "openssl-devel",
    "font-util-devel",
    "xkbcomp-devel",
    "xorgproto",
    "xtrans",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
    "libxcvt-devel",
]
checkdepends = ["xkeyboard-config"]
# check if this needs to be updated when updating
depends = [
    "xserver-xorg-protocol>=20180227",
    "xkeyboard-config",
]
provides = [
    "xserver-abi-extension=10.0",
    "xserver-abi-input=24.4",
    "xserver-abi-video=25.2",
]
pkgdesc = "X.org X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND BSD-3-Clause"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/xorg-server-{pkgver}/xserver-xorg-server-{pkgver}.tar.gz"
sha256 = "c9f87720d663b04a4f6dee03c437b487e53ff6f716e4555489e70131d9ca3317"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-D__uid_t=uid_t", "-D__gid_t=gid_t"],
    "LDFLAGS": ["-Wl,-z,lazy"],  # must be set for modules to work
}
file_modes = {"usr/libexec/Xorg.wrap": ("root", "root", 0o4755)}
# FIXME int
hardening = ["!int"]
# test times out
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["-Dint10=x86emu"]
    case _:
        configure_args += ["-Dint10=false"]

_fontpaths = []

for _fp in ["misc", "100dpi:unscaled", "75dpi:unscaled", "TTF", "Type1"]:
    _fontpaths.append(f"/usr/share/fonts/{_fp}")

configure_args.append("-Ddefault_font_path=" + ",".join(_fontpaths))


def post_install(self):
    self.install_license("COPYING")

    self.chmod(self.destdir / "usr/libexec/Xorg.wrap", mode=0o4755)
    # provided by xserver-xorg-protocol
    self.uninstall("usr/lib/xorg/protocol.txt")
    # from debian: https://salsa.debian.org/xorg-team/xserver/xorg-server
    # check debian/local/xvfb-run for updates as needed
    # note ours is slightly patched (non-GNU fmt(1))
    self.install_bin(self.files_path / "xvfb-run")
    self.install_man(self.files_path / "xvfb-run.1")


@subpackage("xserver-xorg-xnest")
def _(self):
    self.pkgdesc = "Nested X server that runs as an X application"

    return ["usr/bin/Xnest", "usr/share/man/man1/Xnest.1"]


@subpackage("xserver-xorg-xephyr")
def _(self):
    self.pkgdesc = "X server outputting to a window on a pre-existing display"

    return ["usr/bin/Xephyr", "usr/share/man/man1/Xephyr.1"]


@subpackage("xserver-xorg-xvfb")
def _(self):
    self.pkgdesc = "Virtual framebuffer X server"
    self.depends += ["xkeyboard-config", "xauth", "ugetopt"]

    return [
        "usr/bin/Xvfb",
        "usr/bin/xvfb-run",
        "usr/share/man/man1/Xvfb.1",
        "usr/share/man/man1/xvfb-run.1",
    ]


@subpackage("xserver-xorg-devel")
def _(self):
    self.depends += [
        "xorgproto",
        "xtrans",
        "libxfont2-devel",
        "libxkbfile-devel",
        "libxshmfence-devel",
        "libxcb-devel",
        "libxrender-devel",
        "libxrandr-devel",
        "libxi-devel",
        "libpciaccess-devel",
    ]
    return self.default_devel()
