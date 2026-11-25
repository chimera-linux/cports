pkgname = "llvm"
pkgver = "23.1.6"
_majver = pkgver[0:2]
pkgrel = 0
build_style = "meta"
depends = [
    f"llvm{_majver}-default",
    self.with_pkgver("llvm-libs"),
    self.with_pkgver("llvm-binutils"),
    self.with_pkgver("llvm-runtimes"),
]
# providers for autopkgs since this used to be not a metapackage
# we can't use renames because those subpkgs are missing
# facilitate smooth transition
provides = [
    self.with_pkgver("llvm-doc"),
    self.with_pkgver("llvm-runtime"),
    self.with_pkgver("llvm-tools"),
]
pkgdesc = "Low Level Virtual Machine"
license = "custom:meta"
url = "https://llvm.org"
# mostly metapackages
options = ["bootstrap", "!ci", "!check", "!distlicense", "empty"]

# matches the specific llvm package
_enable_mlir = self.stage >= 2 and not self.profile.cross
_enable_flang = _enable_mlir and self.profile.wordsize == 64

# desc use-default has-dbg has-static cond internal-deps provides
_subpkgs = {
    "clang-tools-extra": (
        "extra Clang tools",
        True,  # use-default
        True,  # has-dbg
        True,  # cond
        ["clang"],
        ["clang-tools-extra-static"],
    ),
    "llvm-binutils": (
        "binary manipulation tools",
        True,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        [],
    ),
    "clang": (
        "C language family frontend",
        True,  # use-default
        True,  # has-dbg
        True,  # cond
        ["", "binutils", "clang-rt-devel", "lld"],
        [],
    ),
    "clang-rt-devel": (
        "Clang runtime development files",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        [],
    ),
    "clang-devel": (
        "Clang development files",
        False,  # use-default
        False,  # has-dbg
        True,  # cond
        ["clang-rt-devel"],
        ["clang-devel-static"],
    ),
    "clang-analyzer": (
        "source code analysis",
        True,  # use-default
        False,  # has-dbg
        True,  # cond
        ["clang"],
        [],
    ),
    "clang-libs": (
        "Clang runtime library",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        ["libclang"],
    ),
    "clang-cpp-libs": (
        "Clang C++ runtime library",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        ["libclang-cpp"],
    ),
    "flang": (
        "Fortran frontend",
        True,  # use-default
        True,  # has-dbg
        _enable_flang,
        ["clang", "flang-devel"],
        [],
    ),
    "flang-devel": (
        "Flang development files",
        False,  # use-default
        False,  # has-dbg
        _enable_flang,
        [],
        ["flang-devel-static"],
    ),
    "mlir": ("MLIR", True, True, _enable_mlir, [], []),
    "mlir-devel": (
        "MLIR development files",
        False,  # use-default
        False,  # has-dbg
        _enable_mlir,
        [],
        ["mlir-devel-static"],
    ),
    "mlir-libs": (
        "MLIR runtime libraries",
        False,  # use-default
        True,  # has-dbg
        _enable_mlir,
        [],
        ["libmlir"],
    ),
    "llvm-libs": (
        "LLVM runtime libraries",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        [
            "libllvm",
            "llvm-linker-tools",
        ],
    ),
    "lld": ("linker", True, True, True, [], []),
    "lld-devel": (
        "linker development files",
        False,  # use-default
        False,  # has-dbg
        True,  # cond
        ["lld"],
        ["lld-devel-static"],
    ),
    "llvm-devel": (
        "LLVM development files",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [""],
        ["llvm-devel-static"],
    ),
    "llvm-runtimes": (
        "runtimes",
        False,  # use-default
        True,  # has-dbg
        True,  # cond
        [],
        [],
    ),
    "llvm-runtimes-devel": (
        "runtimes development files",
        False,  # use-default
        False,  # has-dbg
        True,  # cond
        [],
        [
            "libcxx-devel",
            "libcxxabi-devel",
            "libunwind-devel",
        ],
    ),
    "llvm-runtimes-devel-static": (
        "runtimes static libraries",
        False,  # use-default
        False,  # has-dbg
        True,  # cond
        ["runtimes-devel"],
        [
            "libcxx-devel-static",
            "libcxxabi-devel-static",
            "libunwind-devel-static",
        ],
    ),
}


def _genpkg(
    pkg,
    sname,
    desc,
    use_default,
    gen_dbg,
    enable,
    internal_deps,
    provides,
):
    if not sname.startswith("llvm-"):
        rsname = f"llvm-{sname}"
    else:
        rsname = sname
        sname = sname.removeprefix("llvm-")

    @subpackage(rsname, enable)
    def _(self):
        self.subdesc = desc
        self.depends = []
        self.provides = []
        self.options = ["empty"]
        # the real provider
        if use_default:
            self.depends.append(f"llvm{_majver}-{sname}-default")
        else:
            self.depends.append(f"llvm{_majver}-{sname}")
        # parent package for static
        if sname.endswith("-static"):
            self.depends.append(
                f"llvm{_majver}-{sname.removesuffix('-static')}"
            )
        # any additional internal dependencies
        for dep in internal_deps:
            if len(dep) == 0:
                self.depends.append(self.parent)
            else:
                self.depends.append(self.with_pkgver(f"llvm-{dep}"))
        # any extra providers
        if not sname.startswith("llvm-"):
            self.provides.append(self.with_pkgver(sname))
        for prov in provides:
            self.provides.append(self.with_pkgver(prov))

        return []

    if not gen_dbg:
        return

    @subpackage(f"{rsname}-dbg", enable and pkg.build_dbg)
    def _(self):
        self.subdec = "{desc} debug files"
        self.depends = [
            self.with_pkgver(rsname),
            f"llvm{_majver}-{sname}-dbg",
        ]
        self.provides = []
        self.options = ["empty"]
        # any extra providers
        if not sname.startswith("llvm-"):
            self.provides.append(self.with_pkgver(f"{sname}-dbg"))
        for prov in provides:
            self.provides.append(self.with_pkgver(f"{prov}-dbg"))

        return []


@split("dbg", self.build_dbg)
def _(self):
    self.depends = [self.parent, f"llvm{_majver}-dbg"]
    self.provides = [
        self.with_pkgver("llvm-runtime-dbg"),
        self.with_pkgver("llvm-tools-dbg"),
    ]
    self.options = ["empty"]

    return []


for _sname, _pdesc in _subpkgs.items():
    _genpkg(self, _sname, *_pdesc)
